================
What Does It Do?
================

In a website, there is a robots.txt file, which tells web crawlers which files
they should and shouldn't access. This project interprets this file into a computer
understandable format.

=============
How to Use It
=============

Make sure you have the requests module installed. If not, install it with pip3 install
requests.

Then download this file and move it into your project directory. Then import this file.

To use it, run the interpretRobots function, with the root domain (ex 
https://example.com/ or http://example2.com) passed in as an argument

This file will return an array in this format:
[dict: user-agents, list: sitemap]
The dict: user-agents is formatted like this:
{user-id: "allowed": [], "disAllowed": []}


Here is an example usage:
.. code-block:: python
    import robotsinterpret;

    a = robotsinterpret.interpretRobots("http://example.com");
    print("Allowed files for useragent *: ", a[1]["*"]["allowed"]);
    print("Disallowed files for useragent *: ", a[1]["*"]["disAllowed"]);
    print("Sitemaps: ", a[2])
