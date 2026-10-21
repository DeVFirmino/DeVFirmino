<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo-light.svg" alt="daniel dias" width="300">
</picture>

[**Website**](https://danieldias.dev/en) · [**Blog**](https://danieldias.dev/en/blog) · [**Email**](mailto:daanspfc@gmail.com)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lead-dark.svg">
  <img src="assets/lead-light.svg" alt=".NET Developer building practical web applications and APIs with C#, ASP.NET Core and SQL." width="518">
</picture>

Software developer focused on backend .NET. I build APIs and run the live projects below.

</div>


## Projects

### [AI Meter](https://github.com/DeVFirmino/ai-meter)

Two teams share one AI. Every answer adds to that team's bill, and when one team reaches its limit the other keeps going.

<a href="https://github.com/DeVFirmino/ai-meter"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/aimeter-still.png">
  <img src="assets/how-it-works/aimeter.gif" alt="Animation: two teams ask an AI questions, each answer adds to that team's row on the meter, engineering reaches its limit and support keeps going." width="100%">
</picture></a>

ASP.NET Core lab that meters LLM token usage, estimated cost, failures and latency per team with OpenTelemetry and Grafana. Each team has its own request limit: once its window is spent the API answers 429 with `Retry-After`, while the other teams keep theirs.<br>
[Source](https://github.com/DeVFirmino/ai-meter) · [Blog post](https://danieldias.dev/en/blog/ai-meter-usage-and-cost-per-team) · [Lab guide](https://github.com/DeVFirmino/ai-meter/blob/main/docs/lab-guide.md)<br>
<sub>.NET · OPENTELEMETRY · GRAFANA · AI · Simulated usage, no real spending</sub>

### [Sports Betting API](https://github.com/DeVFirmino/SportsBetting) [![CI](https://github.com/DeVFirmino/SportsBetting/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/DeVFirmino/SportsBetting/actions/workflows/ci.yml)

Tap Bet twice by accident and you are charged once, and two bets at the same moment can't spend the same balance.

<a href="https://github.com/DeVFirmino/SportsBetting"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/sportsbetting-still.png">
  <img src="assets/how-it-works/sportsbetting.gif" alt="Animation: you tap Bet twice by accident and the bet is saved once, leaving one bet and €10." width="100%">
</picture></a>

API in .NET 10 for one betting flow: deposit, choose a fixture, place a bet. The wallet debit and the bet commit together, a `rowversion` stops two requests spending the same balance, and a repeated idempotency key never debits twice.<br>
[Live API ↗](https://sportsbetting-api.nicewave-b8afa4cf.westeurope.azurecontainerapps.io/swagger/index.html) (scales to zero) · [Source](https://github.com/DeVFirmino/SportsBetting) · Tests: [concurrent bets against real SQL Server](https://github.com/DeVFirmino/SportsBetting/blob/develop/tests/Integration.Test/PlaceBetUseCaseTests.cs) · [Deployment notes](https://github.com/DeVFirmino/SportsBetting#deployment)<br>
<sub>.NET · ASP.NET CORE · SQL SERVER · AZURE · Deployed by hand to Azure Container Apps with Azure SQL in September 2026</sub>

### [PayMaestro](https://github.com/DeVFirmino/PayMaestro) [![CI](https://github.com/DeVFirmino/PayMaestro/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DeVFirmino/PayMaestro/actions/workflows/ci.yml)

When one payment provider says no, it tries the next one, and you are never charged twice.

<a href="https://github.com/DeVFirmino/PayMaestro"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/paymaestro-still.png">
  <img src="assets/how-it-works/paymaestro.gif" alt="Animation: the first provider declines, PayMaestro tries the next one and you are charged once." width="100%">
</picture></a>

One API in front of several simulated payment gateways. It reserves the idempotency key before calling any gateway and moves to the next gateway on a soft decline. It stops on a hard decline, and when a charge gets no answer it checks that charge with the provider instead of charging again.<br>
[Source](https://github.com/DeVFirmino/PayMaestro) · Tests: [idempotency race](https://github.com/DeVFirmino/PayMaestro/blob/main/tests/PayMaestro.Tests/IdempotencyReservationTests.cs) · [reconciliation](https://github.com/DeVFirmino/PayMaestro/blob/main/tests/PayMaestro.Tests/ReconciliationTests.cs)<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE · Simulated providers, no real money</sub>

### [Fleet Analytics](https://github.com/DeVFirmino/FleetAnalytics)

Vans report where they are as they drive; the kilometres add up, and speeding goes on the van's record.

<a href="https://github.com/DeVFirmino/FleetAnalytics"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/fleetanalytics-still.png">
  <img src="assets/how-it-works/fleetanalytics.gif" alt="Animation: a van sends its location and going over 80 km/h puts a speeding alert on its record." width="100%">
</picture></a>

Vehicle telemetry API. Each GPS reading adds the distance driven to the odometer and raises an alert when the vehicle speeds or is due for a service. The reading, its alerts and the odometer update commit in one transaction.<br>
[Source](https://github.com/DeVFirmino/FleetAnalytics) · Tests: [a failure after the alert is staged saves nothing](https://github.com/DeVFirmino/FleetAnalytics/blob/master/tests/FleetAnalytics.Tests/Services/TripLogIngestionAtomicityTests.cs)<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

### [URL Shortener](https://github.com/DeVFirmino/UrlShortner) [![CI](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml)

Turns a long link into a short one that opens the right page for whoever taps it.

<a href="https://github.com/DeVFirmino/UrlShortner"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/urlshortner-still.png">
  <img src="assets/how-it-works/urlshortner.gif" alt="Animation: a long link becomes a short one, you send it to a friend and they land on the original page." width="100%">
</picture></a>

Three stateless .NET replicas behind nginx, Redis cache-aside in front of Cassandra and collision handling for short codes, all started with one Docker Compose command.<br>
[Source](https://github.com/DeVFirmino/UrlShortner)<br>
<sub>.NET · REDIS · CASSANDRA · DOCKER</sub>

### [danieldias.dev](https://danieldias.dev/en)

My site and blog, in five languages.

<a href="https://danieldias.dev/en"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/how-it-works/danielsite-still.png">
  <img src="assets/how-it-works/danielsite.gif" alt="Animation: a new post goes up on a phone, it comes in five languages, the reader taps Malta's flag and the whole post switches to Maltese. Dani Bot helped translate every edition." width="100%">
</picture></a>

The .NET site I build and run. A local tool turns a draft into five language editions and validates each one before it opens a pull request. CI audits the dependencies, and the metrics endpoint sits behind a token.<br>
[Live site ↗](https://danieldias.dev/en) · Source private<br>
<sub>.NET · RAZOR PAGES · MARKDOWN · DOCKER</sub>

<details>
<summary><b>Three more projects</b></summary>

<br>

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
  <img src="assets/blog-banner.gif" alt="Dani Bot types a post, it rises out of his laptop and fans out into English, Portuguese, Italian, French and Maltese editions, and a done seal lands on the stack." width="100%">
</picture></a>

.NET, Azure, AI and system design, in English, Portuguese, Italian, French and Maltese. [Read the blog ↗](https://danieldias.dev/en/blog) · [RSS](https://danieldias.dev/en/blog/feed.xml)

<p><img src="assets/readme-blog/header.svg" alt="From the blog. Latest articles." width="520"></p>

<!-- BLOG-POST-LIST:START -->
<p>
<a href="https://danieldias.dev/en/blog/how-brazil-counts-125-million-votes-in-one-night"><img src="assets/readme-blog/post-1.svg" alt="Half a million small databases: how Brazil counts 125 million votes in one night. 10 Oct 2026 · 10 MIN." width="400"></a>
<a href="https://danieldias.dev/en/blog/troubleshooting-from-the-1950s-to-2026"><img src="assets/readme-blog/post-2.svg" alt="How troubleshooting changed from the 1950s to 2026. 3 Oct 2026 · 16 MIN." width="400"></a>
</p>
<p>
<a href="https://danieldias.dev/en/blog/azure-cosmos-db-for-rag-benefits-and-when-to-choose-it"><img src="assets/readme-blog/post-3.svg" alt="Azure Cosmos DB for RAG: benefits and when to choose it over a relational database. 29 Sep 2026 · 7 MIN." width="400"></a>
<a href="https://danieldias.dev/en/blog/kubernetes-taints-and-tolerations"><img src="assets/readme-blog/post-4.svg" alt="Kubernetes taints and tolerations explained with a theme park. 22 Sep 2026 · 3 MIN." width="400"></a>
</p>
<p>
<a href="https://danieldias.dev/en/blog/ask-the-model-to-update-the-harness"><img src="assets/readme-blog/post-5.svg" alt="When the LLM gets lost, ask it to update the harness. 17 Sep 2026 · 6 MIN." width="400"></a>
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
