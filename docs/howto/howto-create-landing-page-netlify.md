# HOWTO Create a landing page on Netlify

## Introduction

This document is a detailed walkthrough of the steps performed to create a landing page on <https://baroloteam.online>.

## Step-by-step instructions

### Register a domain name

Choose your preferred domain registrar and buy an available domain.

In our example I logged into <https://register.it> and purchased `baroloteam.online`.

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/33bfb7f4-a414-4374-b22e-bf176a9bb3a2)

### Create a project on Netlify

Login to <https://www.netlify.com/> (or Sign up if you do not have an account yet).

You should be redirected to this page:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/1a29390f-839c-4b07-8b76-e8741608acd3)

In the "Sites" panel, click **Add a new site**

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/0ee33ff0-4b5d-4fa4-9b15-2ed271034fec)

If you already have a source project select the first option and provide the requested information.

In our case [baroloteam.online#1](https://github.com/B-AROL-O/baroloteam.online/issues/1) was still open so I chose **Start from a template** instead.

A few templates will be proposed which you can start from:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/231c0625-3ae8-4541-af1e-1933b98e4cfd)

Choose one proposed template, or click **Browse more templates** to expand the list.

If you are still not satisfied, [Google is your friend](https://www.google.com/search?q=html+simple+landing+page+templates+free) :wink:

You may also revert your previous choice and click the "[Import from a Git repository](https://app.netlify.com/start)" link.

<!-- In our example, I chose the "Bejamas Next.js Blog Starter": [Live demo](https://bejamas-nextjs-blog.netlify.app/), [Source code](https://github.com/netlify-templates/nextjs-blog-theme). -->

In our example, I chose the "Gatsby E-commerce Theme": [Live demo](https://gatsby-ecommerce-theme.netlify.app/), [Source code](https://github.com/netlify-templates/gatsby-ecommerce-theme).

You will be presented with the following choices

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/499bf39d-c6ee-43f8-ac2c-cdd663609cff)

Click **Clone to GitHub**, then in section "Set up your site"

* Team: (accept default)
* Repository settings:
  * Repository name: gatsby-ecommerce-theme
  * Repository visibility: Public

then click **Deploy site**.

This command will create a new public repository <https://github.com/gmacario/gatsby-ecommerce-theme> on GitHub, then will start building the site.

If the build is successful you should be presented a page like this:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/c15b7916-1fa8-4769-9e60-bd7359257da2)

Click on the **Open production deploy** link and browse the site which has been generated.

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/75645a6d-6e69-46e7-9727-490abd78ade1)

### Apply a template to a source repository

We can easily apply template "[gatsby-ecommerce-theme](https://github.com/netlify-templates/gatsby-ecommerce-theme)" to the source repository "[baroloteam.online](https://github.com/B-AROL-O/baroloteam.online)" using the following shell commands

```bash
# Clone source repository
mkdir -p ~/github/B-AROL-O
cd ~/github/B-AROL-O
git clone https://github.com/B-AROL-O/baroloteam.online

# Add a git remote for the template repository
cd ~/github/B-AROL-O/baroloteam.online
git remote add template https://github.com/netlify-templates/gatsby-ecommerce-theme
git fetch --all --prune

# Create a feature branch
git checkout main
git pull --all --prune
git checkout -b feat/apply-gatsby-template
git merge --allow-unrelated-histories template/main
```

The last command may return errors, such as

```text
gianpaolo.macario@HW2457 MINGW64 ~/github/B-AROL-O/baroloteam.online (feat/apply-gatsby-template)
$ git merge --allow-unrelated-histories template/main
Auto-merging README.md
CONFLICT (add/add): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

gianpaolo.macario@HW2457 MINGW64 ~/github/B-AROL-O/baroloteam.online (feat/apply-gatsby-template|MERGING)
$
```

If so, inspect the problems with `git status` then

```bash
git status
vi README.md # Reconcile merge conflicts
git add -A
git commit -sm "Manually merge with template/main"
```

### Update site contents

You may update the contents of the site by pushing new commits on the main branch of the source repository.

### Configure Google Analytics

Please refer to [HOWTO Configure Google Analytics](howto-configure-google-analytics.md) for details.

TODO

### Deploy to official URL

TODO

<!-- EOF -->