## How do I use GitHub?
![Recordit GIF](images/huh-confused.gif)


## Things you need to do to get started:

Create an account in github: [link](https://github.com/join) 

Install github (please follow the instructions for your OS): [link](https://github.com/git-guides/install-git)

Create a personal token [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) 

### Getting & Creating Projects

| Command | Description |
| ------- | ----------- |
| `git init` | Initialize a local Git repository |
| `git clone ssh://git@github.com/[username]/[repository-name].git` | Create a local copy of a remote repository |

### Basic commands

| Command | Description |
| ------- | ----------- |
| `git status` | Check status |
| `git add [file-name.txt]` | Add a file to the staging area |
| `git add -A` | Add all new and changed files to the staging area |
| `git commit -m "[commit message]"` | Commit changes |
| `git rm -r [file-name.txt]` | Remove a file (or folder) |

For a more complete cheat sheet, check the [link](https://education.github.com/git-cheat-sheet-education.pdf)

#### Let's try it out!: 
1. Go to our repo: https://tinyurl.com/INP2021-BC

2. Fork the repository (check here for more details) [link](https://docs.github.com/en/get-started/quickstart/fork-a-repo))
![fork-a-repo](images/fork_button.jpeg)

3. Clone your repo:
```bash
$ git clone https://github.com/YOUR-USERNAME/INP_2021_Git_Intro.git
```
![clone](images/https-url-clone.png)

4. Get into the folder:
```bash
$ cd INP_2021_Git_Intro
```

5. Add a photo of you to `photos` with the filename as `Firstname_Lastname.jpeg`

6. Check your modifications
```bash
$ git status
```

7. Add your modifications
```bash
$ git add -A
```

8. Commit your chages
```bash
$ git commit -m "[commit message]"
```

9. Push your changes
```bash
$ git push
```

10. [BONUS] Create a pull request back to Antonio's repository 
![pull_req](images/pull-request-start-review-button.png)