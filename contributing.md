
# Contributing

## Index
1. [How to contribute? Step by step guide](#how-to-contribute?-step-by-step-guide)
2. [PR conventions](#pr-conventions)
3. [PR review rules](#pr-review-rules)
4. [Issue guidelines](#issue-guidelines)
5. [References](#references)

## How to contribute? Step by step guide

#### Terms
  * Upstream: the repository from the `original_author`
  * Origin: the forked repository under your `account`

#### 1. Fork a `project` to your GitHub `account`

#### 2. Clone the `project` to your local environment
```
    git clone git@github.com:account/project.git
    cd project
```

#### 3. Set up the origin and upstream of the your local `project`
```  
   #  Add the "upstream" to your cloned repository
    git remote add upstream git@github.com:original_author/project.git

   # Add the "origin" to your cloned repository
    git remote add origin git@github.com:account/project.git
```

#### 4. Synchronize with updates from the upstream
```
   # 1) Go to the "master" branch of your fork ("origin")
    git checkout master

   # 2) Fetch the commits from the "upstream"
    git fetch upstream

   # 3) If you have local changes, stash the changes of your "master" branch
    git stash

   # 4) Merge the changes from the "master" branch of the "upstream" into your the "master" branch of your "origin"
    git merge upstream/master

   # 5) Resolve merge conflicts if any and commit your merge
    git commit -m "Merged from upstream"

   # 6) Push the changes to your fork ("origin")
    git push

   # 7) Get back your stashed changes (if any)
    git stash pop
```

#### 5. Do your work in a `new-branch` of your origin
```
   # 1) Add a new branch from your origin/master branch
   git branch new-branch origin/master
   git checkout new-branch

   # 2) Make a commit of your work (e.g. you added your name in the README.md)
   git add README.md
   git commit -m 'add my name'

   # 3) If you had multiple commits, but you want to select a specific commit(e.g. commit id: bbb909f) for a pull request
   git cherry-pick bbb909f

   # 4) Push to your new-branch
   git push origin new-branch
```

#### 6. Send a pull request on GitHub
 * Go to the `new-branch` of your forked `project`
 * Click `Compare & pull request`
 * Leave a comment
   * If you are solving an issue (e.g. `#17`), add `Closes #17` in the comment, the issue will automatically be closed when the pull request is merged.

#### 7. Delete branch locally and/or remotely after pull request is merged on GitHub
 * Deleting your local branch from the command line: `git branch -d new-branch`
 * Additionally if you want to delete your remote branch: `git push origin : new-branch`

## PR conventions
When submitting a PR, please add one of the following prefixes depending on the topic you are addressing:

    [ENH]: Enhancement, new functionality
    [BUG]: Bug fix
    [DOC]: Additions/updates to documentation
    [TST]: Additions/updates to tests
    [BLD]: Updates to the build process/scripts
    [PERF]: Performance improvement
    [CLN]: Code cleanup

In addition:
- Please reference the relevant GitHub issues in your commit message using GH1234 or #1234.
- Include a subject line with < 80 chars.
- Optionally, include a commit message body, leaving one blank line with the subject line.

## PR review rules
 * Input from two reviewers is needed to merge a pull request. One reviewer approves the merge and the other reviewer merges the pull request.

## Issue guidelines

### New issue
Discovering an issue is great, here's what you need to do when you discover an issue:
* Search if the issue has already been created.
* If yes and open refer to existing issue.
* If yes and closed reopen issue with descriptive comment.
* If no, create the issue by:
   * Following our issue [template.](https://github.com/pandas-dev/pandas/blob/master/.github/ISSUE_TEMPLATE.md)

### Existing issue
* Read comments.
* Find out if anyone is working on it, if no, offer to do it. If yes, see if you can be of help.

### Reporting bugs
* Give information about the version and the operating system you are running.
* Show the steps to reproduce bug.
* Add log.

## References
* [GitHub forking](https://gist.github.com/Chaser324/ce0505fbed06b947d962)  
* [Git cherry-pick](https://git-scm.com/docs/git-cherry-pick)
* [Pandas contributing guides](https://pandas.pydata.org/pandas-docs/stable/development/contributing.html)
* To read more tips on how to open issues, PRs and do code reviews, read the things we have been learning throughout the mentoring program [here](https://github.com/python-sprints/pandas-mentoring/blob/master/LEARNING_POINTS.md).
