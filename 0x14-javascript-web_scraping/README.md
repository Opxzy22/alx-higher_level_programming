<!DOCTYPE html>
<html lang="en">
  <head>
   <h1 class="gap"> JavaScript - Web scraping</h1>
</head>
<body>
  <h2> BACKGROUND </h2>
   <p> This is a web scarping project where we are dealing with the following concepts:
  <ol> 
   <li>JSON data manipulation </li>
   <li> request and fetch API </li>
   <li> Read and write using fs module </li>
 </p>

 <h2>RESOURCES</h2>

<p><strong>READ or WATCH</strong>:</p>  
<ul>
<li><a href="/rltoken/ONv-sSv-FA87Mc5rMZmO6A" title="Working with JSON data" target="_blank">Working with JSON data</a> </li>
<li><a href="/rltoken/zm0h7FqpQCZZpPZqxxwLxA" title="The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco" target="_blank">The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco</a> </li>
<li><a href="/rltoken/goymbxGy-cTc5ZdKBTUcTQ" title="request module" target="_blank">request module</a> </li>
<li><a href="/rltoken/j2PStAUtVPdXKwrrFxpt0g" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>
<h2>KNOWLEDGE TEST</h2>
<li>Why JavaScript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>
<h2>REQUIREMENTS</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using <code>node</code> (version 14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="/rltoken/W9rASrTqkF-xXjcwomrMLw" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/GXh9DyGGivUB7pdq9Oqmzg" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/NZR55f9vk1dZXj5q7UI5mQ" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>
<h2>NECESSARY PACKS TO GET STARTED</h2>

<h3>Install Node 14</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="/rltoken/GXh9DyGGivUB7pdq9Oqmzg" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

<h3>Install <code>request</code> module and use it</h3>

<p><a href="/rltoken/goymbxGy-cTc5ZdKBTUcTQ" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>

<p><strong>Notes:</strong> Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it&rsquo;s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).</p>
 <h2 class="gap">TASKS MANDATORY</h2>

<h3 class="panel-title">
      0. Readme
</h3>
 <p>Write a script that reads and prints the content of a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The content of the file must be read in <code>utf-8</code></li>
<li>If an error occurred during the reading, print the error object</li>
</ul>

<h3 class="panel-title">
      1. Write me
</h3>
  <p>Write a script that writes a string to a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The second argument is the string to write</li>
<li>The content of the file must be written in <code>utf-8</code></li>
<li>If an error occurred during while writing, print the error object</li>
</ul>
<h3 class="panel-title">
      2. Status code
</h3>
 <p>Write a script that display the status code of a <code>GET</code> request.</p>

<ul>
<li>The first argument is the URL to request (<code>GET</code>)</li>
<li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
<li>You must use the module <code>request</code></li>
</ul>
<h3 class="panel-title">
      3. Star wars movie title
</h3>
<p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p>

<ul>
<li>The first argument is the movie ID</li>
<li>You must use the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">Star wars API</a> with the endpoint <code>https://swapi-api.alx-tools.com/api/films/:id</code></li>
<li>You must use the module <code>request</code></li>
</ul>
<h3 class="panel-title">
      4. Star wars Wedge Antilles
</h3>
<ul>
<li>The first argument is the API URL of the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">Star wars API</a>: <code>https://swapi-api.alx-tools.com/api/films/</code></li>
<li>Wedge Antilles is character ID <code>18</code> - your script <strong>must</strong> use this ID for filtering the result of the API</li>
<li>You must use the module <code>request</code></li>
</ul>
<h3 class="panel-title">
      5. Loripsum
</h3>
   <p>Write a script that gets the contents of a webpage and stores it in a file.</p>

<ul>
<li>The first argument is the URL to request</li>
<li>The second argument the file path to store the body response</li>
<li>The file must be UTF-8 encoded</li>
<li>You must use the module <code>request</code></li>
</ul>
<h3 class="panel-title">
      6. How many completed?
</h3>
 <p>Write a script that computes the number of tasks completed by user id.</p>

<ul>
<li>The first argument is the API URL: <code>https://jsonplaceholder.typicode.com/todos</code></li>
<li>Only print users with completed task</li>
<li>You must use the module <code>request</code></li>
</ul>

 <h2 class="gap">TASKS ADVANCED</h2>
<h3 class="panel-title">
      7. Who was playing in this movie?
</h3>
<p>Write a script that prints all characters of a Star Wars movie:</p>

<ul>
<li>The first argument is the Movie ID - example: <code>3</code> = &ldquo;Return of the Jedi&rdquo; </li>
<li>Display one character name by line</li>
<li>You must use the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">Star wars API</a></li>
<li>You must use the module <code>request</code></li>
</ul>
<h3 class="panel-title">
      8. Right order
</h3>
<p>Write a script that prints all characters of a Star Wars movie:</p>

<ul>
<li>The first argument is the Movie ID - example: <code>3</code> = &ldquo;Return of the Jedi&rdquo; </li>
<li>Display one character name by line <strong>in the same order of the list &ldquo;characters&rdquo; in the <code>/films/</code> response</strong></li>
<li>You must use the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">Star wars API</a></li>
<li>You must use the module <code>request</code></li>
</ul>
 </body>
</html>
