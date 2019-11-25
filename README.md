# Walk and talk 4 men.

This website will belong to the mens mental health charity Walk and talk 4 men. A young charity in its infancy, it wants to be simple and straight forward with a capability allowing people associated with the charity to easily upload information on the blog. It should feel bright and fun but still informative and sensible.

## UX
 
My website is for two people. Firstly, it is for participants, people interested in joining the activities and finding out about W&T4M and then secondly, the website is going to be used by staff and admin members associated with the charity to upload events and blogs of what has been happening.

People want to know what W&T4M is, dates and locations of events, who to contact if they want to join a walk or create their own and  i think it would also be useful to have some relevant information to help those who might be struggling at the moment however W&T4M is a club and not a medical institution and so we’d only ever refer or quote those more qualified in mental illnesses. With multiple pages for contact, links and a blog i believe we can achieve all of the things i have mentioned with ease.

If someone wants to know what Walk and talk 4 men is on the ‘home’ page there is a brief description and video explaining.

If someone wants to contact W&T4M the email address for the founder can be found by clicking on the ‘contact’ box in the Navbar.

If someone wants to read about previous events and view upcoming dates of different activities this can be found in the ‘blog’ section of the website by clicking on the ‘blog’ box in the navbar.

To find out more information about mental health our ‘links’ page which can be found in by clicking the navbar contains information of various charities and blogs that someone suffering my find useful. They can click on the hyperlink and be taken through to the associated website.

The website includes all of the social media link in the footer. By clicking on the appropriate icon you will be taken to the associated social website for W&T4M.

The search in the top right corner picks up key words in the title of the blogs and will take you to the blog with what you are looking for.

<img src="/dev/trydjango/src/static/image/wireframe.jpg" class="center-img">

## Features

- Feature 1 - The blog page has the backend capability to Create, Read, Edit and Delete. People associated with the charity can be giving an admin login where they can access the backend tool to upload their on blog page.

- Feature 2 - The search box allows people to type in a word and if that word is used it the title of a blog that blog will be displayed. 

- Feature 3 - On the home page there is an explainer video to summarise the work of the charity. 


### Existing Features
- Feature 1 - allows admin users to create blog posts, by adding information and picture to the creat new blog page.

Feature 2 - allows the club members to type in a world they’re interested in reading about and if that word occurs in the title of a blog the blog will come up.
Feature 3 - allows new members to click play on the video and be able to watch a video explaining exactly what W&T4M is.

At the moment the search box isn’t particularly helpful because there are not many blogs to make it relevant however over time and more and more things get posts this will become useful.

### Features Left to Implement
In the future i would like to implement a mailing list so that we can keep track of all our members and their details.
When W&T4M is a registered charity it might always be useful to set up an e-commerce website to help raise money to put back in to its events and/or a place where they can donate to a cause.

## Technologies Used


- [Cloud9]('https://aws.amazon.com/cloud9/')
    - The project uses **Cloud9** as its development environment.

- [Github]('https://github.com/eddiebrett/walkandtalk4men1')
    - The project uses **Github** to upload its files/code to be stored and shared on the internet.

- [Heroku](‘www.heroku.com’)
    - The project uses **Heroku** to host the websites and its detabase.

- [S3]('https://aws.amazon.com/free/storage/?trk=ps_a131L000005OOOyQAO&trkCampaign=UK&sc_channel=PS&sc_campaign=acquisition_UK&sc_publisher=Google&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|UK|EN|Text&sc_content=s3_e&sc_detail=amazon%20s3&sc_category=S3&sc_segment=293639776553&sc_matchtype=e&sc_country=UK&s_kwcid=AL!4422!3!293639776553!e!!g!!amazon%20s3&ef_id=CjwKCAjwxt_tBRAXEiwAENY8hT4CUoqYpVz4zBRxHT_u0h-tSuMorLa00PPt3hAtlidMVaxpDxiNwhoCYE4QAvD_BwE:G:s')
    - The project uses **S3** to store the pictures and files in the cloud.

- [google domain]('https://domains.google/intl/en-GB/?utm_source=google&utm_medium=cpc&utm_campaign=emea-gb-all-en-dr-bkws-all-all-signup-b-domains-1005575%20&utm_content=text-ad-none-none-DEV_c-CRE_329515079986-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+BMM+%7C+%5B1:1%5D+Google+Domain-KWID_43700049254276848-aud-625929750375:kwd-22740955676-userloc_9045244&utm_term=KW_%2Bgoogle%20%2Bdomain-ST_%2Bgoogle+%2Bdomain&gclid=CjwKCAjwxt_tBRAXEiwAENY8hTPTEpYGMlT962X_lwZbOg_zeG_Yp1UR-tdODlvY4c_FUkLRF1Pc0xoC6wsQAvD_BwE')
    - The project uses **Google domain** to give it a unique URL page.

- [HTML]('https://html.com/')
    - The project uses **HTML** to give meaning and structure the website.

- [CSS]('https://developer.mozilla.org/en-US/docs/Web/CSS')
    - The project uses **CSS** to style the site.

- [Python]('https://www.python.org/')
    - The project uses **Python** as its programming language to develope the web application.

- [Django]('https://www.djangoproject.com/')
    - The project uses **Django** as its framework to develop the python script.



## Testing

To test this website i shared the link around for different people to try and give feedback on. It was at this point that we noticed the edit and delete buttons were viewable to everyone and so i changed the views.py page in the blog app to only let admin users see this.

Because most of the links are used multiple times from one source “navbar.html”, “base.html”, “footer.html” it meant that there was less chance for bugs to occur and so if the links worked on one page they would for all.

I typed keywords in to the search box to see if any blogs became available of which at first there wasn’t and so i knew i had to fix this.

I inspected the site in google chrome to ensure that the mobile version of the app was functional as intended.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

I took inspiration for the bright colours and large fonts used in the site from the charity artwork work and logos to create a uniformed image of the company. The mind UK website gave me the confidence to employ the bright colours as at first i was worried they mate have been a bit childish for the target demographic but seeing as the mind charity is the because in the country apparently it is suitable. 

### Content
All content is original.

### Media
The photos used in this site were obtained from the Walk and Talk facebook page and the founder.

The Video used in this site was obtained from my own youtube channel ‘https://www.youtube.com/watch?v=iRwgFKViEGM’.



### Acknowledgements

I received inspiration for this project from https://www.mind.org.uk

I received inspiration for this project from https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12041s

I built this website whilst watching a youtube video called python for beginners and so some of the code may be similar: https://www.youtube.com/watch?v=F5mRW0jo-U4&t=12044s