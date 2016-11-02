:title: Pelican based blogging
:author: BabuSubashChandar
:date: 2016-11-02
:category: Technology
:tags: Pelican, Blogging, how-to
:image: static/images/pelican.png
:summary: It is always a painstaking process to fall into visious cycle of blogging through wordpress, blogger or other blogging framework...

--------------

|Pelican|

Consider this as my opinion on blogging, someone might find it harsh
when their blogging mechanisms are ridiculed. It is always a
painstaking process for me to write something on the blogger or
wordpress. I was maintaining, "was" (put that in a double double
quotes) a literature blog, my poetic scribblings. Out of the blue,
that blog was orphaned. Then there was this technology blog hosted on
wordpress. I had posted a single article, again this was not fed
properly by me. Because of a lot of formatting, looking for a nice theme
along and lot more. It was just given away and I lost all my interest
to write at all. Even the teensy-tiny bit of writer in me died so
long. Then this saviour, a static site generator, Pelican came for the
rescue.

People were speaking high about static site creators, there are
numerous such frameworks. Pelican is one among them, a framework
written in Python. I got instant cling on to this and tried it out.

Okay! Lets get into business.

----------------

What this is about?
-------------------

This article speaks about how can one write their thoughts out just in
a text document, forgetting all those formatting, rolling all the way
down the hill to fit that in a template and so on. Albeit there is an
overhead in choosing a theme for this framework, if you are not
concerned about the looks much, you could use one of the available
themes in Github. Oh, FYI, Pelican as well as its themes along with
the goodies are all available in Github.

----------------

How it is done?
---------------

This wonderful Python based framework, Pelican is available as a pip
package. For the uninitiated, pip is a commandline tool to install
python based software packages. The following steps would kickstart a
pelican blog. The steps are for a Linux desktop.

-----------------

Installation
~~~~~~~~~~~~

.. code:: bash

  ~$ pip install --user pelican

The code snippet will install pelican for the current user.

-----------------

Kickstart
~~~~~~~~~

.. code:: bash

  ~$ pelican-quickstart

  Welcome to pelican-quickstart v3.6.3.

  This script will help you create a new Pelican-based website.

  Please answer the following questions so this script can generate the files
  needed by Pelican.


  > Where do you want to create your new web site? [.]
  > What will be the title of this web site? test
  > Who will be the author of this web site? test
  > What will be the default language of this web site? [en]
  > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)
  > What is your URL prefix? (see above example; no trailing slash) http://example.com
  > Do you want to enable article pagination? (Y/n)
  > How many articles per page do you want? [10]
  > What is your time zone? [Europe/Paris]
  > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
  > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
  > Do you want to upload your website using FTP? (y/N) n
  > Do you want to upload your website using SSH? (y/N) n
  > Do you want to upload your website using Dropbox? (y/N) n
  > Do you want to upload your website using S3? (y/N) n
  > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
  > Do you want to upload your website using GitHub Pages? (y/N) y
  > Is this your personal page (username.github.io)? (y/N) y
  Done. Your new project is available at /tmp/test


With this a static site can be generated in a local machine. The folder structure will be as follows.

.. code:: bash

  ~$ tree .
  .
  ├── content
  ├── develop_server.sh
  ├── fabfile.py
  ├── Makefile
  ├── output
  ├── pelicanconf.py
  └── publishconf.py

  2 directories, 5 files

In the above list, the following are the meanings.

.. table::
   :class: no-border

   =================   =====================================================
   content             holds all the articles.
   develop_server.sh   a shell script to run a http server locally.
   fabfile.py          deploys the same in a server.
   Makefile            compiles the text files to html files.
   output              holds all the css and html files for the static site.
   pelicanconf.py      configuration for Pelican.
   publishconf.py      configuration to publish the site.
   =================   =====================================================

-----------------

Start blogging
~~~~~~~~~~~~~~

Add content to the above 'content' directory in any of the
friendly format (`Markdown
<https://daringfireball.net/projects/markdown/basics>`__ or
`ReStructured Text format
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`__). After
this, host the output directory's content to your domain or using
github. Refer how to host a blog using Travis article `here <https://babuenir.github.io/blog/hosting-blog-using-travis.html>`__.

**Happy Blogging!**

References
----------

- `Pelican documentation <http://docs.getpelican.com/en/stable/>`__

-----------------

Credits
-------

- The Pelican image is from
  `Pixabay. <https://pixabay.com/en/pelican-bird-flying-wings-fauna-30878/>`__. Actually
  the project lacks a logo.

-----------------

.. |Pelican| image:: static/images/pelican.png
   :width: 300
