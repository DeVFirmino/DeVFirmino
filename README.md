<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
  <img src="assets/logo-light.svg" alt="daniel dias" width="300">
</picture>

[**Website**](https://danieldias.dev/en) · [**Blog**](https://danieldias.dev/en/blog) · [**LinkedIn**](https://www.linkedin.com/in/daniel-dias-504168113/) · [**Email**](mailto:daanspfc@gmail.com)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lead-dark.svg">
  <img src="assets/lead-light.svg" alt=".NET Developer building practical web applications and APIs with C#, ASP.NET Core and SQL." width="518">
</picture>

Software developer focused on backend .NET. I build APIs and run the live projects below.

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/credentials-dark.png">
  <img src="assets/credentials-light.png" alt="Education: Technology Degree in Systems Analysis and Development (UniFatecie, Brazil, QQI Level 6); Higher Diploma in Computing (SETU, Ireland, QQI Level 7). Languages spoken: PT, EN, IT, FR (A2)." width="100%">
</picture>

## Tech

**Backend**

![C#](https://img.shields.io/badge/C%23-E8DCC4?style=flat-square&logo=csharp&logoColor=26211C)
![.NET](https://img.shields.io/badge/.NET-E8DCC4?style=flat-square&logo=dotnet&logoColor=26211C)
![ASP.NET Core](https://img.shields.io/badge/ASP.NET_Core-E8DCC4?style=flat-square&logo=dotnet&logoColor=26211C)
![EF Core](https://img.shields.io/badge/EF_Core-E8DCC4?style=flat-square&logo=nuget&logoColor=26211C)

**Data**

![SQL Server](https://img.shields.io/badge/SQL_Server-E8DCC4?style=flat-square&logo=microsoftsqlserver&logoColor=26211C)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-E8DCC4?style=flat-square&logo=postgresql&logoColor=26211C)
![Redis](https://img.shields.io/badge/Redis-E8DCC4?style=flat-square&logo=redis&logoColor=26211C)

**Cloud & CI**

![Azure](https://img.shields.io/badge/Azure-E8DCC4?style=flat-square&logo=microsoftazure&logoColor=26211C)
![Docker](https://img.shields.io/badge/Docker-E8DCC4?style=flat-square&logo=docker&logoColor=26211C)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-E8DCC4?style=flat-square&logo=githubactions&logoColor=26211C)
![AZ-900](https://img.shields.io/badge/AZ--900_Certified-E8DCC4?style=flat-square&logo=microsoftazure&logoColor=26211C)

**Interfaces in my projects**

![TypeScript](https://img.shields.io/badge/TypeScript-E8DCC4?style=flat-square&logo=typescript&logoColor=26211C)
![React](https://img.shields.io/badge/React-E8DCC4?style=flat-square&logo=react&logoColor=26211C)

## Projects

[**Sports Betting API**](https://github.com/DeVFirmino/SportsBetting) [![CI](https://github.com/DeVFirmino/SportsBetting/actions/workflows/ci.yml/badge.svg?branch=develop)](https://github.com/DeVFirmino/SportsBetting/actions/workflows/ci.yml)<br>
API in .NET 10 for one betting flow: deposit, choose a fixture, place a bet. The wallet debit and the bet commit together, a `rowversion` stops two requests spending the same balance, and a repeated idempotency key never debits twice.<br>
Tests: [concurrent bets against real SQL Server](https://github.com/DeVFirmino/SportsBetting/blob/develop/tests/Integration.Test/PlaceBetUseCaseTests.cs)<br>
<sub>.NET · ASP.NET CORE · SQL SERVER · AZURE · Deployed by hand to Azure Container Apps with Azure SQL in September 2026 · [Live API](https://sportsbetting-api.nicewave-b8afa4cf.westeurope.azurecontainerapps.io/swagger/index.html), scales to zero · [deployment notes](https://github.com/DeVFirmino/SportsBetting#deployment)</sub>

[**PayMaestro**](https://github.com/DeVFirmino/PayMaestro) [![CI](https://github.com/DeVFirmino/PayMaestro/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DeVFirmino/PayMaestro/actions/workflows/ci.yml)<br>
One API in front of several simulated payment gateways. It reserves the idempotency key before any gateway call, moves to the next gateway on a soft decline, stops on a hard decline or a charge with no answer, and reconciles that charge with the provider instead of charging again.<br>
Tests: [idempotency race](https://github.com/DeVFirmino/PayMaestro/blob/main/tests/PayMaestro.Tests/IdempotencyReservationTests.cs) · [reconciliation](https://github.com/DeVFirmino/PayMaestro/blob/main/tests/PayMaestro.Tests/ReconciliationTests.cs)<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

[**Fleet Analytics**](https://github.com/DeVFirmino/FleetAnalytics)<br>
Vehicle telemetry API. Each GPS reading adds the distance driven to the odometer and raises an alert when the vehicle speeds or is due for a service. The reading, its alerts and the odometer update commit in one transaction.<br>
Tests: [a failure after the alert is staged saves nothing](https://github.com/DeVFirmino/FleetAnalytics/blob/master/tests/FleetAnalytics.Tests/Services/TripLogIngestionAtomicityTests.cs)<br>
<sub>.NET · ASP.NET CORE · EF CORE · SQLITE</sub>

[**danieldias.dev**](https://danieldias.dev/en)<br>
The .NET site I build and run, with a blog in five languages. A local tool turns a draft into five language editions and validates each one before it opens a pull request. CI audits the dependencies, and the metrics endpoint sits behind a token.<br>
<sub>.NET · RAZOR PAGES · MARKDOWN · DOCKER · Source private</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-maltese-dark.png">
  <img src="assets/card-maltese-light.png" alt="Maltese Transcriber, featured, live portfolio project. Live Maltese-to-English transcription for people trying to better understand everyday conversations. .NET, TypeScript, React, SignalR." width="100%">
</picture>

[**Open live site ↗**](https://maltesetranscriber.mt) · <sub>Source private</sub>

[**URL Shortener**](https://github.com/DeVFirmino/UrlShortner) [![CI](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/DeVFirmino/UrlShortner/actions/workflows/ci.yml)<br>
Three stateless .NET replicas behind nginx, Redis cache-aside in front of Cassandra and collision handling for short codes, all started with one Docker Compose command.<br>
<sub>.NET · REDIS · CASSANDRA · DOCKER</sub>

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

<a href="https://danieldias.dev/en/blog"><img src="assets/blog-banner.gif" alt="Dani Bot types a post, it rises out of his laptop and fans out into English, Portuguese, Italian, French and Maltese editions, and a done seal lands on the stack." width="100%"></a>

.NET, Azure, AI and system design, in English, Portuguese, Italian, French and Maltese. [Read the blog ↗](https://danieldias.dev/en/blog) · [RSS](https://danieldias.dev/en/blog/feed.xml)

**Latest posts**

<!-- BLOG-POST-LIST:START -->
- [Half a million small databases: how Brazil counts 125 million votes in one night](https://danieldias.dev/en/blog/how-brazil-counts-125-million-votes-in-one-night) · Oct 2026
- [How troubleshooting changed from the 1950s to 2026](https://danieldias.dev/en/blog/troubleshooting-from-the-1950s-to-2026) · Oct 2026
- [Azure Cosmos DB for RAG: benefits and when to choose it over a relational database](https://danieldias.dev/en/blog/azure-cosmos-db-for-rag-benefits-and-when-to-choose-it) · Sep 2026
- [Kubernetes taints and tolerations explained with a theme park](https://danieldias.dev/en/blog/kubernetes-taints-and-tolerations) · Sep 2026
- [When the LLM gets lost, ask it to update the harness](https://danieldias.dev/en/blog/ask-the-model-to-update-the-harness) · Sep 2026<!-- BLOG-POST-LIST:END -->

**Code that goes with the posts**

<a href="https://github.com/DeVFirmino/kubectl-by-example">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/card-kubectl-dark.png">
    <img src="assets/card-kubectl-light.png" alt="kubectl by example — imperative kubectl commands, one CKAD section at a time, each run on a throwaway kind cluster with the real output and the YAML that a dry run generates. Kubernetes, kubectl, CKAD." width="100%">
  </picture>
</a>

<a href="https://github.com/DeVFirmino/dotnet-opentelemetry-search">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/card-otel-dark.png">
    <img src="assets/card-otel-light.png" alt="OpenTelemetry demo — a one-route ASP.NET Core API built to show what OpenTelemetry records on its own across traces, metrics and logs, and the one attribute the application has to declare itself. .NET, ASP.NET Core, OpenTelemetry." width="100%">
  </picture>
</a>

<a href="https://github.com/DeVFirmino/ai-meter">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/card-ai-meter-dark.png">
    <img src="assets/card-ai-meter-light.png" alt="AI Meter — an ASP.NET Core lab that meters LLM token usage, estimated cost, failures and latency per team with OpenTelemetry and Grafana, and gives each team its own request quota. .NET, OpenTelemetry, Grafana, AI." width="100%">
  </picture>
</a>

[**LLM harness example**](https://github.com/DeVFirmino/llm-harness-example) — the files an LLM reads before it answers, kept in a repository and updated by review. Goes with [When the LLM gets lost, ask it to update the harness](https://danieldias.dev/en/blog/ask-the-model-to-update-the-harness).

[**AZ-900 Study Guide**](https://github.com/DeVFirmino/AZ900-Studies) — Azure Fundamentals from the concepts up, not memorised answers. Goes with [How I passed AZ-900](https://danieldias.dev/en/blog/how-i-passed-az-900).

## Contact

I'm open to backend .NET roles and freelance projects involving APIs and integrations.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/open-to-work-dark.png">
  <img src="assets/open-to-work-light.png" alt="Open to software roles, freelance projects and collaborations." width="470">
</picture>

[<img src="assets/cta-linkedin.png" alt="LinkedIn" height="32">](https://www.linkedin.com/in/daniel-dias-504168113/)
[<img src="assets/cta-email.png" alt="Email" height="32">](mailto:daanspfc@gmail.com)
[<img src="assets/cta-website.png" alt="Website" height="32">](https://danieldias.dev/en)
