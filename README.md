# StartupJobs

# Sources

The Sources table contains various websites that we crawl. These sources have an
associated crawler associated. Most of the time these crawlers are RSS feeds,
but we also have custom crawlers that are connected to the ProfileName. Ever 30
mins, a cron job runs that checks against these sources for new job posts and
adds them to the JobPosts table

- `ops-prod makeprospect_hn`
  - Move to job_post_sources_hn
- `ops-prod makeprospect_rss`
  - Move to job_post_sources_rss

# Terms

- Term is Correct
- RejectedTerm
- RejectedAIOrgs
- RejectedUrl

# JobPosts

JobPosts table is powered through a Kanban. Most of it is automated with a few
parts which are manual. The table goes through a combination of AI, MTurk, and
Reviewers while continuously adding new leads to the CRM.

## Uncategorized (Automated)

- `ops-prod makeprospect_job_posts_qualify_uncategorized`
- The Uncategorized status is where all job posts go into by default. Whenever,
  we qualify against uncategorized we do the following:
  - Check that it doesn't have a RejectedTerm in the Notes. A RejectedTerm is
    something like a company that posts as lot of job posts, a country, etc. that
    aren't relevant to us.
  - Run the Notes against an AI that tries to find the Company name. We check
    against this Organization name within our CRM. If it does find it we move it
    to Draft (AI) otherwise we move it to Draft.
  - We check that it isn't a RejectedUrl. If it is we move it to Draft.
- yco success sales sourcing job-posts crawl
- yco success sales sourcing job-posts qualify-uncategorized
  - Crawlers for Different Locations

## Draft (AI / Automated)

- `ops-prod makeprospect_job_posts_qualify_ai_draft`
  - Move to just job_posts_qualify_ai_draft
- `ops-prod makeprospect_jobs_run`
  - Move to just job_posts_run
- The Draft (AI) is where items go if the Company Name has been found through
  the AI. However, we don't always trust the AI for new items so we check against
  our CRM.
- If the Company Name doesn't exist within our CRM then we move it to Draft
  status, while clearing the fields. Furthermore, we add this Company Name into
  the Terms table to ensure that the term is not Invalid.
- If it does exist we get the details from the CRM, add it to the record and
  move it to the Live status. We then check to see if it has a relevant term that
  will make was reach out to them and adds a task and a note for the Prospecting
  team to do outreach in the CRM.

## Working (MTurk / Automated)

## Finished (MTurk / Automated)

## Error

## Manual

## Approved

## Rejected

## Live

- `ops-prod prospect_add_to_sendowl`
