<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo-light.svg" alt="daniel dias" width="300">
</picture>

[**Website**](https://danieldias.dev/en) · [**Blog**](https://danieldias.dev/en/blog) · [**Email**](mailto:daanspfc@gmail.com)

<a href="https://danieldias.dev/en"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-still.png">
  <img src="assets/hero.gif" alt="Dani Bot holds a coffee in front of a hand-drawn skyline of monuments while the windmill and the big wheel turn." width="100%">
</picture></a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lead-dark.svg">
  <img src="assets/lead-light.svg" alt=".NET Developer building practical web applications and APIs with C#, ASP.NET Core and SQL." width="518">
</picture>

Software developer focused on backend .NET. I build APIs and run the live projects below.

</div>


## Projects

### [LearnTranscriber](https://github.com/DeVFirmino/learntranscriber) [![CI](https://github.com/DeVFirmino/learntranscriber/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/DeVFirmino/learntranscriber/actions/workflows/ci.yml)

Read a class or a meeting as it is said, and ask about it without pausing.

<a href="https://github.com/DeVFirmino/learntranscriber"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/learntranscriber-still.png">
  <img src="assets/how-it-works/learntranscriber.webp" alt="Animation: an online English class plays on a MacBook while the floating assistant answers when to use for and since." width="100%">
</picture></a>

Open-source macOS app in Electron, React and Swift. Speech is transcribed on the Mac with Apple Speech or a local Whisper server, or by a cloud service; a floating assistant answers with the AI you choose (a ChatGPT sign-in, an API key or a local model), and sessions stay in a local SQLite database.<br>
[Download for Mac ↗](https://github.com/DeVFirmino/learntranscriber/releases/latest/download/LearnTranscriber-arm64.dmg) · [Homebrew](https://github.com/learntranscriber/homebrew-tap) · [Website](https://learntranscriber.danieldias.dev) · [Source](https://github.com/DeVFirmino/learntranscriber) · [How it works](https://github.com/DeVFirmino/learntranscriber#how-it-works)<br>
<sub>ELECTRON · REACT · SWIFT · AI · Free and open source under the MIT license</sub>

### [racha-bot](https://github.com/DeVFirmino/racha-bot) [![CI](https://github.com/DeVFirmino/racha-bot/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DeVFirmino/racha-bot/actions/workflows/ci.yml)

The weekly football list goes round the WhatsApp group, and two fair teams come back in seconds.

<a href="https://github.com/DeVFirmino/racha-bot"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/rachabot-still.png">
  <img src="assets/how-it-works/rachabot.webp" alt="Animation: the weekly list arrives in the WhatsApp group, each player ticks their name once they have paid, the organiser sends !sortear and the bot answers with a card of two teams." width="100%">
</picture></a>

WhatsApp bot in .NET 10 for a weekly pickup game. It reads the group's list the way people already write it, checks who has paid and draws two balanced teams with a goalkeeper in each, sent back as an image card drawn with ImageSharp. It connects through a self-hosted WAHA gateway, checks the signature on every webhook and answers only commands; a local simulator shows the card without a WhatsApp number.<br>
[Source](https://github.com/DeVFirmino/racha-bot) · [Try it without WhatsApp](https://github.com/DeVFirmino/racha-bot#teste-em-1-minuto-sem-whatsapp) (in Portuguese)<br>
<sub>.NET · WHATSAPP · IMAGESHARP · DOCKER · Free and open source under the MIT license</sub>

### Ocllo

Ocllo sits in the Mac's notch while your AI assistant writes code. You answer it there, and each finished turn gets a second opinion.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/ocllo-still.png">
  <img src="assets/how-it-works/ocllo.webp" alt="Animation: on a MacBook an AI assistant edits code in the terminal, a card drops from Ocllo's island in the notch asking to run the tests, you click Allow, and the finished card says Looks good." width="100%">
</picture>

macOS companion in Swift for Claude Code, Codex and Copilot CLI. The agents report their sessions to Ocllo on the Mac through their own hooks; a permission or a question drops from the notch as a card you can answer, and Claude, on your own account, gives each finished turn a short verdict. Nothing is sent for review until you allow it for that project.<br>
Source private<br>
<sub>SWIFT · MACOS · REACT · AI · In progress, no public download yet</sub>

### Catidea

Volunteers count the cats at each colony from their phone, and the team sees how every colony changes over time.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/catidea-still.png">
  <img src="assets/how-it-works/catidea.webp" alt="Animation: five street cats eat from a bowl while a volunteer counts them on the phone, two clipped ears are ringed as already neutered, the count is saved and the colony's chart gains today's bar." width="100%">
</picture>

Census platform for groups that look after street cat colonies. A count records what one person saw and is never edited, the share of ear-tipped cats is the headline number because it tracks how many are already neutered, and colony locations stay behind a sign-in. ASP.NET Core with EF Core on PostGIS, a React and TypeScript client, and reports in CSV and PDF.<br>
Source private<br>
<sub>.NET · POSTGIS · REACT · TYPESCRIPT</sub>

### [AI Meter](https://github.com/DeVFirmino/ai-meter)

Two teams share one AI. Every answer adds to that team's bill, and when one team reaches its limit the other keeps going.

<a href="https://github.com/DeVFirmino/ai-meter"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/aimeter-still.png">
  <img src="assets/how-it-works/aimeter.webp" alt="Animation: two teams ask an AI questions, each answer adds to that team's row on the meter, engineering reaches its limit and support keeps going." width="100%">
</picture></a>

ASP.NET Core lab that meters LLM token usage, estimated cost, failures and latency per team with OpenTelemetry and Grafana. Each team has its own request limit: once its window is spent the API answers 429 with `Retry-After`, while the other teams keep theirs.<br>
[Source](https://github.com/DeVFirmino/ai-meter) · [Blog post](https://danieldias.dev/en/blog/ai-meter-usage-and-cost-per-team) · [Lab guide](https://github.com/DeVFirmino/ai-meter/blob/main/docs/lab-guide.md)<br>
<sub>.NET · OPENTELEMETRY · GRAFANA · AI · Simulated usage, no real spending</sub>

### [URL Shortener](https://github.com/DeVFirmino/UrlShortner) [![CI](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml)

Turns a long link into a short one that opens the right page for whoever taps it.

<a href="https://github.com/DeVFirmino/UrlShortner"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/urlshortner-still.png">
  <img src="assets/how-it-works/urlshortner.webp" alt="Animation: a long link becomes a short one, you send it to a friend and they land on the original page." width="100%">
</picture></a>

Three stateless .NET replicas behind nginx, Redis cache-aside in front of Cassandra and collision handling for short codes, all started with one Docker Compose command.<br>
[Source](https://github.com/DeVFirmino/UrlShortner)<br>
<sub>.NET · REDIS · CASSANDRA · DOCKER</sub>

### [danieldias.dev](https://danieldias.dev/en)

My site and blog, in five languages.

<a href="https://danieldias.dev/en"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/danielsite-still.png">
  <img src="assets/how-it-works/danielsite.webp" alt="Animation: a new post goes up on a phone, it comes in five languages, the reader taps Malta's flag and the whole post switches to Maltese. Dani Bot helped translate every edition." width="100%">
</picture></a>

The .NET site I build and run. A local tool turns a draft into five language editions and validates each one before it opens a pull request. CI audits the dependencies, and the metrics endpoint sits behind a token.<br>
[Live site ↗](https://danieldias.dev/en) · Source private<br>
<sub>.NET · RAZOR PAGES · MARKDOWN · DOCKER</sub>

<details>
<summary><b>Six more projects</b></summary>

<br>

[**Sports Betting API**](https://github.com/DeVFirmino/SportsBetting) — betting API where tapping Bet twice by accident charges you once, and two bets at the same moment can't spend the same balance. [Live API ↗](https://sportsbetting-api.nicewave-b8afa4cf.westeurope.azurecontainerapps.io/swagger/index.html) (scales to zero)<br>
<sub>.NET · ASP.NET CORE · SQL SERVER · AZURE</sub>

[**PayMaestro**](https://github.com/DeVFirmino/PayMaestro) — one API in front of several simulated payment gateways. When one provider says no it tries the next, and it never charges twice.<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

[**Fleet Analytics**](https://github.com/DeVFirmino/FleetAnalytics) — vehicle telemetry API. Each GPS reading adds to the odometer and raises speeding and service alerts in the same transaction.<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

[**Good Hamburger**](https://github.com/DeVFirmino/good-hamburger) — order management API with combo discount rules, domain-level invariants and integration tests.<br>
<sub>.NET · ASP.NET CORE · EF CORE · XUNIT</sub>

[**Book Management**](https://github.com/DeVFirmino/BookManagment) — MVC library lending app. Session action filters keep clients out of the admin pages, and only an administrator can open the client list. That last filter is tested for an administrator, a client and a visitor with no session.<br>
<sub>.NET · ASP.NET CORE MVC · EF CORE · SQL</sub>

[**Portfolio Manager**](https://github.com/DeVFirmino/AvaloniaPortifolioManager) — desktop app for clients, investment portfolios, holdings and transactions, built with Avalonia and EF Core.<br>
<sub>.NET · AVALONIA · EF CORE · SQL</sub>

</details>

## Blog

<a href="https://danieldias.dev/en/blog"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/blog-banner-still.png">
  <img src="assets/blog-banner.webp" alt="Dani Bot types a post, it rises out of his laptop and fans out into English, Portuguese, Italian, French and Maltese editions, and a done seal lands on the stack." width="100%">
</picture></a>

.NET, Azure, AI and system design, in English, Portuguese, Italian, French and Maltese. [Read the blog ↗](https://danieldias.dev/en/blog) · [RSS](https://danieldias.dev/en/blog/feed.xml)

<p><img src="assets/readme-blog/header.svg" alt="From the blog. Latest articles." width="520"></p>

<!-- BLOG-POST-LIST:START -->
<p>
<a href="https://danieldias.dev/en/blog/one-bot-one-job-tidying-up-grok-bots"><img src="assets/readme-blog/post-1.svg" alt="How to organise your Grok Bots: one bot, one job. 10 Nov 2026 · 6 MIN." width="400"></a>
<a href="https://danieldias.dev/en/blog/one-agent-loop-or-many"><img src="assets/readme-blog/post-2.svg" alt="One agent loop, or many? A faster run with a missing delivery date. 8 Nov 2026 · 7 MIN." width="400"></a>
</p>
<p>
<a href="https://danieldias.dev/en/blog/october-2026-in-17-security-incidents"><img src="assets/readme-blog/post-3.svg" alt="October 2026 in 17 security incidents, and what they have in common. 30 Oct 2026 · 10 MIN." width="400"></a>
<a href="https://danieldias.dev/en/blog/when-your-rag-pipeline-becomes-an-attack-surface"><img src="assets/readme-blog/post-4.svg" alt="When your RAG pipeline becomes an attack surface. 27 Oct 2026 · 6 MIN." width="400"></a>
</p>
<p>
<a href="https://danieldias.dev/en/blog/how-brazil-counts-125-million-votes-in-one-night"><img src="assets/readme-blog/post-5.svg" alt="Half a million small databases: how Brazil counts 125 million votes in one night. 10 Oct 2026 · 10 MIN." width="400"></a>
</p>
<!-- BLOG-POST-LIST:END -->

<p><strong>Code that goes with the posts</strong></p>
<p><a href="https://github.com/DeVFirmino/kubectl-by-example"><picture>
<source media="(max-width: 600px)" srcset="assets/readme-blog/code-1-phone.svg">
<img src="assets/readme-blog/code-1.svg" width="100%" alt="kubectl by example. Imperative kubectl commands, one CKAD section at a time, each run on a throwaway kind cluster with the real output. GitHub.">
</picture></a></p>
<p><a href="https://github.com/DeVFirmino/dotnet-opentelemetry-search"><picture>
<source media="(max-width: 600px)" srcset="assets/readme-blog/code-2-phone.svg">
<img src="assets/readme-blog/code-2.svg" width="100%" alt="OpenTelemetry demo. A one-route ASP.NET Core API that shows what OpenTelemetry records on its own. GitHub.">
</picture></a></p>
<p><a href="https://github.com/DeVFirmino/llm-harness-example"><picture>
<source media="(max-width: 600px)" srcset="assets/readme-blog/code-4-phone.svg">
<img src="assets/readme-blog/code-4.svg" width="100%" alt="LLM harness example. The files an LLM reads before it answers, kept in a repository and updated by review. GitHub.">
</picture></a></p>
<p><a href="https://github.com/DeVFirmino/AZ900-Studies"><picture>
<source media="(max-width: 600px)" srcset="assets/readme-blog/code-5-phone.svg">
<img src="assets/readme-blog/code-5.svg" width="100%" alt="AZ-900 Study Guide. Azure Fundamentals from the concepts up, not memorised answers. GitHub.">
</picture></a></p>
<details>
<summary>Read the related articles</summary>

<ul><li><a href="https://danieldias.dev/en/blog/kubectl-by-example-part-1-pods">kubectl by example, part 1: pods</a></li><li><a href="https://danieldias.dev/en/blog/opentelemetry-in-dotnet">OpenTelemetry in .NET</a></li><li><a href="https://danieldias.dev/en/blog/ai-meter-usage-and-cost-per-team">AI Meter: run a lab for LLM usage, estimated cost and team limits</a></li><li><a href="https://danieldias.dev/en/blog/ask-the-model-to-update-the-harness">When the LLM gets lost, ask it to update the harness</a></li><li><a href="https://danieldias.dev/en/blog/how-i-passed-az-900">How I passed AZ-900</a></li></ul>

</details>

## Tech

<picture>
  <source media="(max-width: 600px)" srcset="assets/tech-phone.svg">
  <img src="assets/tech.svg" alt="Tech. Backend: C#, .NET, ASP.NET Core, EF Core. Data: SQL Server, PostgreSQL, Redis. Cloud and delivery: Azure, Docker, GitHub Actions. Frontend in my projects: TypeScript, React. AI and agents: RAG, agent orchestration, context engineering, prompt engineering, chatbots; Claude Code, MCP, agent skills, OpenAI." width="100%">
</picture>

<picture>
  <source media="(max-width: 600px)" srcset="assets/credentials-card.svg">
  <img src="assets/credentials-wide.svg" alt="Education and certification: Higher Diploma in Computing, SETU, Ireland, QQI Level 7; Technology Degree in Systems Analysis and Development, UniFatecie, Brazil, QQI Level 6; Microsoft Certified: Azure Fundamentals (AZ-900). Languages: Portuguese, English, Italian, French (A2)." width="100%">
</picture>

## Contact

<img src="assets/contact-card.svg" alt="Open to software roles, freelance projects and collaborations. Dani Bot waves hello." width="100%">

<p align="center">
  <a href="mailto:daanspfc@gmail.com"><img src="assets/cta-email.png" alt="Email" height="36"></a>
</p>
