from databricks.sdk import WorkspaceClient

w = WorkspaceClient(profile="saibhavanipanabaka")

print("Connected as:", w.current_user.me().user_name)

print("\nJobs:")
for j in w.jobs.list():
    print(" -", j.job_id, j.settings.name)

print("\nPipelines:")
for p in w.pipelines.list_pipelines():
    print(" -", p.pipeline_id, p.name)
