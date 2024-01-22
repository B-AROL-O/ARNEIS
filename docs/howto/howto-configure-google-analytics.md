# HOWTO Configure Google Analytics

## Introduction

This document explains how to configure [Google Analytics 4](https://analytics.google.com/analytics/web/?) and integrate it into your existing web site, for instance the one created following the [HOWTO Create a Landing Page on Netlify](howto-create-landing-page-netlify.md).

## Reference documents

<!-- See <https://github.com/SOLARMA/quello-che-vuoi/tree/main/learning/google-startup-school> -->

### A Founders Guide to Google Analytics: Part 1

<!-- (2023-06-29 11:00-11:35 CEST) -->

In this session we'll cover the basics of Google Analytics 4, including how to surface AI driven insights for your customers and how to create and use reports

Presenters:

* [Ainhoa Ybanez](https://www.linkedin.com/in/ainybez/) - Advertising Solutions Architect, Mobile Apps, Google
* [Grant Kemp](https://www.linkedin.com/in/creativetechnologyuk/) - Advertising Solutions Architect, Mobile Apps, Google

<!-- <https://cloudonair.withgoogle.com/events/startup-school/watch?talk=emea-talk6> -->

<!-- <https://www.youtube.com/watch?v=EY6PDUowafE> -->

[![EMEA: The Founders Guide to Google Analytics, Part 1: Getting started](https://img.youtube.com/vi/EY6PDUowafE/0.jpg)](https://www.youtube.com/watch?v=EY6PDUowafE "EMEA: The Founders Guide to Google Analytics, Part 1: Getting started")

### A Founders Guide to Google Analytics: Part 2

<!-- (2023-07-06 11:00-12:00 CEST) -->

In this follow up session, we'll explore workspaces in GA4 and you'll learn how to build custom tables and visualizations of your data

Presenters:

* [Ainhoa Ybanez](https://www.linkedin.com/in/ainybez/) - Advertising Solutions Architect, Mobile Apps, Google
* [Grant Kemp](https://www.linkedin.com/in/creativetechnologyuk/) - Advertising Solutions Architect, Mobile Apps, Google

[![EMEA: The Founders Guide to Google Analytics, Part 2: Exploring your data](https://img.youtube.com/vi/0V99kmrW9EI/0.jpg)](https://www.youtube.com/watch?v=0V99kmrW9EI "EMEA: The Founders Guide to Google Analytics, Part 2: Exploring your data")

## Step-by-step instructions

### Create a new GA4 stream on Google Analytics

Login to <https://analytics.google.com/>

Create a new Analytics Account, or choose an existing one.

Click **Admin**, then **+ Create Property**. The following page should be displayed:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/30786425-513b-44b0-a6e6-9b1222ceb80c)

Fill in the Property details. In our example:

* Property name (Required): `baroloteam`
* Reporting time zone: Italy
* Currency: Euro (€)

then click **Next** and fill in our Business details. In our example:

* Industry category (Required): Hobbies &amp; Leisure
* Business size (Required): Small - 1 to 10 employees

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/ae40cea3-a104-4ef3-9158-e63ce65ce6ce)

Click **Next**, then choose our business objectives.

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/92432c55-320e-4911-b734-47c223ad68f7)

In our example:

* [x] **Generate leads**
* [ ] **Drive online sales**
* [x] **Raise brand awareness**
* [x] **Examine user behavior**
* [ ] **Get baseline reports**

When you are done, click **Create**. The wizard will show the following page:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/b19e37d2-1690-4dfa-8318-2d127b3f5130)

In our example we only choose "Web". We should now set up our web stream.

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/d992d2cd-051d-4dca-9c26-eb7171433f2e)

Fill in the required information - in our example:

* Website URL: <https://baroloteam.online>
* Stream name: baroloteam.online stream
* Enhanced measurements: (leave defaults)

then click **Create stream**. After a few seconds the stream details will be displayed:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/37bad402-844d-4b78-ad15-1e4d6a35b437)

Click **View tag instructions** to display code snippet to be injected into your website.
In our example:

![image](https://github.com/B-AROL-O/ARNEIS/assets/75182/5fe3801f-c21b-413d-b883-2f8046e47771)

### Inject GA4 scripts into a Gatsby site

Reference: <https://www.gatsbyjs.com/docs/how-to/testing/ab-testing-with-google-analytics-and-netlify/>

Edit file `src/components/header.js`

NOTE: For a site based on the <https://github.com/netlify-templates/gatsby-ecommerce-theme> template the file is called `src/components/Header/Header.js`.

TODO

### TODO

<!-- EOF -->