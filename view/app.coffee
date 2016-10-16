express = require 'express'
load = require 'express-load'
# this is part of node.js handling and transforming file paths.
app = express()
app.d3 = require 'd3'
app.jsdom = require 'jsdom'
app.set 'view engine', 'pug'

load("controllers")
  .into(app)

# define where controllers are stored.
main = app.controllers.main

# render home page as the index() controller in the main controller file
app.get '/', main.index

console.log 'server listening on port 8080'

## listen to the server on port 8080
server = app.listen '8080'
