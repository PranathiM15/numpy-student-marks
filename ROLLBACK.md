# Rollback notes

## Keep a known-good version
After a tested change, commit it to Git. The commit history is the rollback record; do not rewrite shared history just to hide a broken deployment.

## Roll back a bad change locally
1. Run `git log --oneline` and identify the commit to undo.
2. Run `git revert <bad-commit-hash>` to create a new commit that reverses the change.
3. Test the app locally, then run `git push`.

For a deployment platform connected to this repository, the new revert commit should trigger a fresh deployment. If the platform provides a previous-deployment rollback control, you may use it as an emergency measure, then revert the source commit so Git and the deployed version stay aligned.

No rollback has been performed for this starter project. Record actual deployment or rollback screenshots only after you perform those actions; do not present this guide as proof that a rollback already happened.
