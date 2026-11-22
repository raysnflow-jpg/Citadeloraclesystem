import { createHmac, timingSafeEqual } from "node:crypto";

const MAX_BODY_BYTES = 1_000_000;

async function readBody(request: Request): Promise<Buffer | null> {
  if (!request.body) return Buffer.alloc(0);

  const reader = request.body.getReader();
  const chunks: Buffer[] = [];
  let totalBytes = 0;

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    totalBytes += value.byteLength;
    if (totalBytes > MAX_BODY_BYTES) {
      await reader.cancel();
      return null;
    }
    chunks.push(Buffer.from(value));
  }

  return Buffer.concat(chunks);
}

export async function GET() {
  return Response.json({ ok: true, endpoint: "/api/webhook" });
}

export async function POST(request: Request) {
  const secret = process.env.GITHUB_WEBHOOK_SECRET;
  if (!secret) {
    return Response.json({ error: "Webhook is not configured" }, { status: 503 });
  }

  const signature = request.headers.get("x-hub-signature-256");
  const event = request.headers.get("x-github-event");
  if (!signature || !event) {
    return Response.json({ error: "Missing GitHub signature or event header" }, { status: 400 });
  }

  const body = await readBody(request);
  if (!body) {
    return Response.json({ error: "Request body exceeds 1 MB" }, { status: 413 });
  }

  const expected = `sha256=${createHmac("sha256", secret).update(body).digest("hex")}`;
  const receivedBuffer = Buffer.from(signature);
  const expectedBuffer = Buffer.from(expected);

  if (
    receivedBuffer.length !== expectedBuffer.length ||
    !timingSafeEqual(receivedBuffer, expectedBuffer)
  ) {
    return Response.json({ error: "Invalid webhook signature" }, { status: 401 });
  }

  return Response.json({ received: true }, { status: 202 });
}
