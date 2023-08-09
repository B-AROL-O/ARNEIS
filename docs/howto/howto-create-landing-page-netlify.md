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

Click **Clone to github**, then in section "Set up your site"

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

TODO

<!-- EOF -->