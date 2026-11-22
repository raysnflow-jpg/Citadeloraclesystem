const setupSteps = [
  "Set GITHUB_WEBHOOK_SECRET in the Vercel project environment variables.",
  "In GitHub, open Settings → Webhooks → Add webhook.",
  "Set the Payload URL to your deployed domain followed by /api/webhook.",
  "Choose application/json and enter the same secret in GitHub.",
  "Select the events to deliver. Valid signed deliveries are acknowledged without side effects.",
];

export function StatusPanel() {
  return (
    <main className="mx-auto flex min-h-screen w-full max-w-6xl flex-col px-5 py-8 sm:px-8 sm:py-12">
      <header className="flex items-center justify-between border-b border-white/10 pb-6">
        <a href="#top" className="text-sm font-semibold tracking-[0.2em] text-white">
          CITADEL <span className="text-lime-300">/</span> ORACLE
        </a>
        <span className="rounded-full border border-lime-300/25 bg-lime-300/10 px-3 py-1.5 text-xs font-medium text-lime-200">
          Webhook receiver
        </span>
      </header>

      <section id="top" className="grid flex-1 items-center gap-12 py-14 lg:grid-cols-[1.15fr_0.85fr] lg:py-20">
        <div>
          <p className="mb-5 text-xs font-semibold uppercase tracking-[0.24em] text-lime-300">
            GitHub integration
          </p>
          <h1 className="max-w-2xl text-4xl font-semibold leading-tight tracking-tight text-white sm:text-6xl">
            A secure endpoint for your GitHub events.
          </h1>
          <p className="mt-6 max-w-xl text-base leading-7 text-slate-300 sm:text-lg">
            This receiver verifies GitHub&apos;s SHA-256 signature and acknowledges valid deliveries. It does not store or act on event payloads.
          </p>
          <div className="mt-9 flex flex-wrap items-center gap-3">
            <span className="rounded-md border border-white/10 bg-white/[0.04] px-3 py-2 font-mono text-sm text-slate-100">
              POST /api/webhook
            </span>
            <span className="text-sm text-slate-400">HMAC-SHA256 verified</span>
          </div>
        </div>

        <aside className="rounded-2xl border border-white/10 bg-slate-900/80 p-6 shadow-2xl shadow-black/20 sm:p-8">
          <div className="flex items-center gap-3">
            <span className="relative flex size-2.5">
              <span className="absolute inline-flex size-full animate-ping rounded-full bg-lime-300 opacity-30" />
              <span className="relative inline-flex size-2.5 rounded-full bg-lime-300" />
            </span>
            <h2 className="text-lg font-semibold text-white">Configure delivery</h2>
          </div>
          <ol className="mt-6 space-y-5">
            {setupSteps.map((step, index) => (
              <li key={step} className="flex gap-4 text-sm leading-6 text-slate-300">
                <span className="flex size-6 shrink-0 items-center justify-center rounded-full bg-white/5 font-mono text-xs text-lime-200">
                  {String(index + 1).padStart(2, "0")}
                </span>
                <span>{step}</span>
              </li>
            ))}
          </ol>
          <div className="mt-7 rounded-lg border border-white/10 bg-black/20 p-4">
            <p className="text-xs font-medium uppercase tracking-wider text-slate-400">Health check</p>
            <code className="mt-2 block text-sm text-slate-100">GET /api/webhook</code>
            <p className="mt-1 text-xs text-slate-500">Returns a simple readiness response.</p>
          </div>
        </aside>
      </section>

      <footer className="flex flex-col gap-2 border-t border-white/10 pt-5 text-xs text-slate-500 sm:flex-row sm:items-center sm:justify-between">
        <span>Project Juniper-33</span>
        <span>Only signed GitHub deliveries are accepted.</span>
      </footer>
    </main>
  );
}
