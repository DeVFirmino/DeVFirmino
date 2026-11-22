<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo-light.svg" alt="daniel dias" width="300">
</picture>

<p>
  <a href="https://danieldias.dev/en"><img src="assets/cta-website.svg" alt="Website" height="36"></a>&nbsp;
  <a href="https://danieldias.dev/en/blog"><img src="assets/cta-blog.svg" alt="Blog" height="36"></a>&nbsp;
  <a href="mailto:daanspfc@gmail.com"><img src="assets/cta-email.svg" alt="Email" height="36"></a>
</p>

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

Read what you hear. Ask as you listen.

<a href="https://github.com/DeVFirmino/learntranscriber"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/learntranscriber-still.png">
  <img src="assets/how-it-works/learntranscriber.webp" alt="Animation: an online English class plays on a MacBook while the floating assistant answers when to use for and since." width="100%">
</picture></a>

I made LearnTranscriber for the moments in a lesson when a phrase goes by before you’ve worked out what it means. The Mac app transcribes as you listen. You can ask about the phrase in a floating panel and revisit the transcript after the lesson.<br>
[Download for Mac ↗](https://github.com/DeVFirmino/learntranscriber/releases/latest/download/LearnTranscriber-arm64.dmg) · [Homebrew](https://github.com/learntranscriber/homebrew-tap) · [Website](https://learntranscriber.danieldias.dev) · [Source](https://github.com/DeVFirmino/learntranscriber) · [How it works](https://github.com/DeVFirmino/learntranscriber#how-it-works)<br>
<sub>ELECTRON · REACT · SWIFT · AI · Free and open source under the MIT license</sub>

### [racha-bot](https://github.com/DeVFirmino/racha-bot) [![CI](https://github.com/DeVFirmino/racha-bot/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DeVFirmino/racha-bot/actions/workflows/ci.yml)

A WhatsApp bot that draws teams from the weekly football list.

<a href="https://github.com/DeVFirmino/racha-bot"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/rachabot-still.png">
  <img src="assets/how-it-works/rachabot.webp" alt="Animation: the weekly list arrives in the WhatsApp group, each player ticks their name once they have paid, the organiser sends !sortear and the bot answers with a card of two teams." width="100%">
</picture></a>

The organiser replies to the group’s list with the draw command. Once everyone has marked their payment, racha-bot posts the teams as an image, with a goalkeeper on each side. The open-source .NET project includes a simulator for trying the draw outside WhatsApp.<br>
[Source](https://github.com/DeVFirmino/racha-bot) · [Try it without WhatsApp](https://github.com/DeVFirmino/racha-bot#teste-em-1-minuto-sem-whatsapp) (in Portuguese)<br>
<sub>.NET · WHATSAPP · IMAGESHARP · DOCKER · Free and open source under the MIT license</sub>

### Ocllo

A macOS app for following coding agents and reading what they changed.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/ocllo-still.png">
  <img src="assets/how-it-works/ocllo.webp" alt="Animation: on a MacBook an AI assistant edits code in the terminal, a card drops from Ocllo's island in the notch asking to run the tests, you click Allow, and the finished card says Looks good." width="100%">
</picture>

When an agent asks a question or needs permission, I can answer from the notch on my Mac. After a turn that adds code, Ocllo can make a card explaining a programming concept with the lines that illustrate it. Sharing code for those cards is opt-in per project.<br>
Source private<br>
<sub>SWIFT · MACOS · REACT · AI · In progress, no public download yet</sub>

### Catidea

A way for volunteers to track counts and neutering in street cat colonies.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/catidea-still.png">
  <img src="assets/how-it-works/catidea.webp" alt="Animation: five street cats eat from a bowl while a volunteer counts them on the phone, two clipped ears are ringed as already neutered, the count is saved and the colony's chart gains today's bar." width="100%">
</picture>

Volunteers can log a count from their phone and note how many cats have a clipped ear tip, a sign they’ve been neutered. Catidea uses counts taken under the same protocol to show trends. The colony map is private.<br>
Source private<br>
<sub>.NET · POSTGIS · REACT · TYPESCRIPT</sub>

### [AI Meter](https://github.com/DeVFirmino/ai-meter)

A lab for seeing how LLM usage adds up by team.

<a href="https://github.com/DeVFirmino/ai-meter"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/aimeter-still.png">
  <img src="assets/how-it-works/aimeter.webp" alt="Animation: two teams ask an AI questions, each answer adds to that team's row on the meter, engineering reaches its limit and support keeps going." width="100%">
</picture></a>

Send requests as different teams and look at their token use and estimated costs in Grafana. Send enough to reach one team’s request limit and compare the results. The lab uses a simulated model.<br>
[Source](https://github.com/DeVFirmino/ai-meter) · [Blog post](https://danieldias.dev/en/blog/ai-meter-usage-and-cost-per-team) · [Lab guide](https://github.com/DeVFirmino/ai-meter/blob/main/docs/lab-guide.md)<br>
<sub>.NET · OPENTELEMETRY · GRAFANA · AI · Simulated usage, no real spending</sub>

### [URL Shortener](https://github.com/DeVFirmino/UrlShortner) [![CI](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml)

A .NET study project that follows a short link from creation to redirect.

<a href="https://github.com/DeVFirmino/UrlShortner"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/urlshortner-still.png">
  <img src="assets/how-it-works/urlshortner.webp" alt="Animation: a long link becomes a short one, you send it to a friend and they land on the original page." width="100%">
</picture></a>

I built this to see how a shortener’s cache and database work together. The app checks Redis for the short code and looks it up in Cassandra if it’s missing. The project runs locally with Docker Compose.<br>
[Source](https://github.com/DeVFirmino/UrlShortner)<br>
<sub>.NET · REDIS · CASSANDRA · DOCKER</sub>

### [danieldias.dev](https://danieldias.dev/en)

My portfolio and a technical blog in five languages.

<a href="https://danieldias.dev/en"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/danielsite-still.png">
  <img src="assets/how-it-works/danielsite.webp" alt="Animation: a new post goes up on a phone, it comes in five languages, the reader taps Malta's flag and the whole post switches to Maltese. Dani Bot helped translate every edition." width="100%">
</picture></a>

Each edition of a post lives in its own Markdown file. I built a local tool to prepare and review the translations before a pull request goes up.<br>
[Live site ↗](https://danieldias.dev/en) · Source private<br>
<sub>.NET · RAZOR PAGES · MARKDOWN · DOCKER</sub>

<details>
<summary><b>Six more projects</b></summary>

<br>

[**Sports Betting API**](https://github.com/DeVFirmino/SportsBetting) — a .NET API for trying the same bet request twice and inspecting the saved bet and wallet balance. [Live API ↗](https://sportsbetting-api.nicewave-b8afa4cf.westeurope.azurecontainerapps.io/swagger/index.html) (scales to zero)<br>
<sub>.NET · ASP.NET CORE · SQL SERVER · AZURE</sub>

[**PayMaestro**](https://github.com/DeVFirmino/PayMaestro) — a .NET example of when a card payment moves to another provider and when a decline ends the attempt.<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

[**Fleet Analytics**](https://github.com/DeVFirmino/FleetAnalytics) — a .NET API that saves each GPS reading in the same transaction as the odometer update and any alerts.<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

[**Good Hamburger**](https://github.com/DeVFirmino/good-hamburger) — a .NET order API that applies combo discounts and stores each item’s price when it’s added to the order.<br>
<sub>.NET · ASP.NET CORE · EF CORE · XUNIT</sub>

[**Book Management**](https://github.com/DeVFirmino/BookManagment) — an ASP.NET Core MVC library app with tests that check who can open the client list.<br>
<sub>.NET · ASP.NET CORE MVC · EF CORE · SQL</sub>

[**Portfolio Manager**](https://github.com/DeVFirmino/AvaloniaPortifolioManager) — an Avalonia app for tracing how an investment portfolio gets from EF Core to the desktop view.<br>
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
  <a href="mailto:daanspfc@gmail.com"><img src="assets/cta-email.svg" alt="Email" height="36"></a>
</p>
