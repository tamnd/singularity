# 12. The site: singularity.tamnd.com

The site is static. `sing site build` writes it from `tamnd/singularity` (the map, the records, the pages, the Lean index) and from the handbook build. The deploy workflow of `tamnd/singularity` puts it on the Cloudflare Worker `singularity`, which has no script and serves the files of `public/`:

```jsonc
// The Worker that serves singularity.tamnd.com. It has no script: Cloudflare serves the files of public/, which sing site build writes.
{
  "name": "singularity",
  "compatibility_date": "2026-11-01",
  "workers_dev": true,
  "routes": [{ "pattern": "singularity.tamnd.com", "custom_domain": true }],
  "assets": {
    "directory": "public",
    "html_handling": "auto-trailing-slash",
    "not_found_handling": "404-page"
  }
}
```

The templates, the CSS and the search start as a copy of riemann-agent's `site/`, so the two sites look like one family.

## 12.1 The home page and its doors

The home page states the problem in one paragraph, the status in one line computed from the records ("dimension 4 in characteristic p: open; known cases formalized: N of M; nodes proved: P of Q"), and offers doors, as riemann does:

| Door | For | Goes to |
|---|---|---|
| I know the mathematics | experts | `/problem/`: the problem, what is known, the routes |
| I referee | anyone who checks a claim | `/trust/` |
| I am a student | learners | `/learn/`: the paths through the handbook |
| I know Lean | Lean users | `/code/`: the package, the statements, how to contribute |
| I am a program | agents and tools | `/llms.txt` and `/api/` |

## 12.2 The pages

| Path | Content | Source |
|---|---|---|
| `/problem/` | the statements of 03, the known results table, the open cases, each with its Lean statement and its fidelity state | `site/problem.md` and `records/` |
| `/map/` | the map as a graph, filtered by tier, route or status; a node opens its page | `blueprint/nodes`, `records/status.json` |
| `/node/<tag>/` | statement, proof sketch, Lean statement and proof (with a link to the source line), uses and used-by, papers, Math 2.0 link, handbook section, history | all of the above |
| `/paper/<key>/` | the paper record: metadata, the results the project uses, their nodes and status | `papers/` |
| `/routes/` and `/routes/<R>/` | each route of 04: the idea, the key obstruction, its nodes and its progress bar | `blueprint/routes.yaml` |
| `/lab/` and `/lab/<run>/` | the computations: spec, environment, results, the node it supports or refutes | `lab/runs/` |
| `/trust/` | the trust table (14) and the fidelity table (06.3) | `records/trust.json`, `records/fidelity.json` |
| `/learn/` | learning paths through the handbook volumes, with links to Math 2.0 | `paths/` |
| `/handbook/` | the volumes, the PDF and EPUB downloads, the HTML chapters | the handbook build |
| `/code/` | the layout of the package, the pinned toolchain, how to build, the statement files in full | `Singularity/`, `lean-toolchain` |
| `/timeline/` | the weekly reports and the releases | `reports/` |
| `/search/` | search over nodes, papers, Lean names and the handbook | built index |
| `/api/nodes.json`, `/api/papers.json`, `/api/status.json` | the data, for programs | `records/` |
| `/llms.txt` | a short text map of the site for language models | generated |

## 12.3 Rules

1. **Every number on the site comes from a record.** No page has a hand-written count or status.
2. **No claim without the trust rows.** The home page and `/problem/` show the status of the open problem from `records/status.json`. If a node of an open problem becomes `proved`, the site shows "Lean proof, checks C1 to Cn passed" and links the trust page. The words "solved" or "proved" for the open problem appear only after the claim policy of 06.6 is met.
3. **Math renders without JavaScript where possible.** KaTeX at build time, as riemann.
4. **`sing site check`** checks every internal link, every node tag, every Lean link (it must resolve to a line of the pinned commit), the style rules, and that each page has a title and a description.
