# Assignment 5 — CI/CD, Docker Packaging and Safe Rollback

**Level:** Intermediate. **Course alignment:** Git/GitHub, CI/CD, Flask/FastAPI, Docker, Kubernetes and cloud deployment.

## Scenario
You are maintaining a small Python API that returns model predictions. The API must be tested automatically, packaged reproducibly and deployed only after its checks pass. Your task is to demonstrate a safe release process using Git branches, pull requests, GitHub Actions and Docker.

## Part A — Git workflow
1. Create a dedicated practice repository or isolated sandbox branch.
2. Clone it with Git CLI and inspect status/history.
3. Create versioned feature branches; edit files, run tests, commit and push.
4. Open pull requests and merge only after checks pass.
5. Tag a stable release and document the commit associated with the tag.

## Part B — GitHub Actions CI
Create a workflow that triggers on push to main, pull requests and manual dispatch. It must check out the repository, set up Python 3.12, install dependencies and run pytest -v. Preserve the test output and explain what a green or red run means.

## Part C — Controlled failure and rollback exercise
In a **disposable practice repository only**, introduce a deliberately incorrect test expectation on a separate branch. Observe the failing pull-request check. For the rollback exercise, follow the instructor's approved sandbox procedure to demonstrate reverting a merged commit with git revert -m 1 and restoring the passing version.

Do not deliberately merge a failing build into a production service, important portfolio default branch or repository used by other people. The purpose is to learn failure diagnosis and rollback mechanics in an isolated environment.

## Part D — Docker packaging
1. Write a Dockerfile that uses a Python base image, copies dependency definitions, installs packages and starts the API.
2. Add .dockerignore to exclude virtual environments, cache files, local credentials and generated test artifacts.
3. Build and run the image locally.
4. Test the API endpoint through its documented URL.
5. Explain image vs container, port mapping, volumes and environment configuration.

## Part E — Cloud architecture reflection
Describe how the image could be deployed to a managed container service such as ECS/Fargate. Compare a long-running service with a one-off task. Explain rolling update vs blue/green deployment, networking/security group requirements, health checks and rollback.

## Deliverables
- Repository with application code and tests
- CI workflow YAML
- Dockerfile and .dockerignore
- Screenshots or links to CI runs (only from your own sandbox work)
- Release tag and rollback explanation
- 500–700 word deployment architecture note

## Assessment rubric (100 points)
| Area | Points |
|---|---:|
| Git CLI, branches, commits and tags | 20 |
| Automated CI workflow and test interpretation | 25 |
| Failure diagnosis and safe rollback | 20 |
| Docker build and local API test | 20 |
| Cloud architecture and security explanation | 15 |

Never commit secrets, model credentials or private customer data. Do not publish screenshots containing tokens or other secrets.
