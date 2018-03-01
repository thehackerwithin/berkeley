# Walkthrough of creating d3_simplemap
The goal is to create a (map)[https://bl.ocks.org/cypranowska/b17359016fd22b81914fd2031cb301f0] of the United States, and bind data of US campsites to it. 

This tutorial begins by opening up index.html, which contains the empty template within which we can make our map. The file should have a few important items to note:

1. HTML tags at the beginning of the document, followed by a set of `<style>` tags, and a set of `<body>` tags. 
2. Within the `<body>` tag, there should be three scripts that are loaded: d3.v3.min.js, topojson.v1.min.js, and d3-queue.v3.min.js. 
3. An additional `<empty>` script tag within which we will write our d3 code.

The data for the US map and the campsites will be from this (gist)[https://gist.github.com/cypranowska/b17359016fd22b81914fd2031cb301f0]

## Step 1: Make an svg canvas, load the .json data
To make a map, we should first create a canvas upon which to draw our svg objects. Let's create a variable called `svg` in the `/* JavaScript goes here */` portion of our html document, and set it's height and width to 1160 px and 960 px, respectively.

```JavaScript
var svg = d3.select("body").append("svg")
            .attr("height", 1160)
            .attr("width", 960);
```

Next, we are going to load our TopoJSON data using the function `d3.json`. Our data are coming from this (gist)[https://gist.github.com/cypranowska/b17359016fd22b81914fd2031cb301f0]. To load the data, find the us.json file on the page, click on 'Raw', and copy the URL. We'll pass the URL to `d3.json`. 

```JavaScript
d3.json("https://gist.githubusercontent.com/cypranowska/b17359016fd22b81914fd2031cb301f0/raw/9fcd2c3e60c74e8ce8d5c2385d2961f06d815bb9/us.json", function(error, us) {
    if (error) return console.error(error);
    console.log(us);
});
```

Serve index.html and check out the JavaScript console. You should see the object printed to the console! But how do we turn the loaded data into an svg? We want to make a path (by virtual selection) and bind the data to it. For map-related data, we need two additional things: 1) we need a path generator and 2) a projection. The path generator takes the 2D shape and draws it on the svg object for the specified projection (the way we flatten a 3D object onto a 2D space).

```JavaScript
d3.json("https://gist.githubusercontent.com/cypranowska/b17359016fd22b81914fd2031cb301f0/raw/9fcd2c3e60c74e8ce8d5c2385d2961f06d815bb9/us.json", function(error, us) {
    if (error) return console.error(error);
    
    svg.append("path")
        .datum(topojson.feature(us, us.objects.states))
        .attr("d", d3.geo.path().projection(d3.geo.mercator()));
});
```
Now if we look at index.html we should see a familiar outline. But it looks a little funny. That's because we chose the (Mercator projection)[https://en.wikipedia.org/wiki/Mercator_projection], a cylindrical map projection. This causes land at the poles to look distended, and the equator to look smushed. Change the method inside `.projection()` to `d3.geo.albersUsa()`. It should look like the familiar rendering of the US map, with Alaska and Hawaii placed at the bottom left corner. 

## Step 2: Add some style

One of the benefits of using SVG is that we can use CSS to change the appearance pretty easily. Before we begin changing the appearance of our map, let's clean up some of our code first. The first step would be to create separate variables for our states.

```JavaScript
var states = topojson.feature(us, us.objects.states);
```

Make height and width their own variables, too. And now for our projection:

```JavaScript
var projection = d3.geo.albersUsa()
                    .scale(width)
                    .translate([height/2, width/2]);
```
This ensures that our projection is scaled and centered compared to our canvas. 

And finally for the path generator:

```JavaScript
var path = d3.geo.path()
                .projection(projection);
```

Now in the `svg.append()` section, we can write:

```JavaScript
svg.append("path")
    .datum(states)
    .attr("d", path);
```

If you look at the text of us.json, you'll find that counties and states are the two types of features in the TopoJSON object. If we want to create a path for each state, then we want to make another call to topojson.feature, extract the `features` array for each, and compute a data join. In addition to creating the path, we can assign each state it's own class, that we can use as a CSS selector

```JavaScript
svg.selectAll("states")
    .data(topojson.feature(us, us.objects.states).feature)
    .enter().append("path")
    .attr("class", function (d) { return "state" + d.id; })
    .attr("d", path);
```
What happens if you enter the following in the CSS portion of the document?

```HTML
.state2 { fill: #ddc; }
```
This method is fine if you want to highlight specific states, but if you want the color of each state the same while still showing the outline of its boundaries, this is way too tedious! Instead what we should do is use `topojson.mesh` which calculates the boundaries of all objects inside the TopoJSON input.


`topojson.mesh` returns two things, the topology and a geometry object (represented as `a` and `b` below). You can pass them to a function to filter out boundaries you don't want to represent in your map. Exterior borders are defined by when the values of the topology and geometry object are the same, and interior borders are defined when they aren't equivalent. 

```JavaScript
svg.append("path")
    .datum(topojson.mesh(us, us.objects.states), 
            function (a,b) { return a !== b })
    .attr("d", path)
    .attr("class", "border");
```
What happens when you now enter `.border { stroke: #fff; }` inside the `<style>` tags?

We can see the border nicely now, but we still want to change the color of states. To do this we are going to append a new object called `g` to our `svg` object, create a path from each feature array for each state, and give it an `id` to use as a CSS selector. We'll also assign the paths with the `topojson.mesh` data to the same id. 

```JavaScript
svg.append("g")
    .attr("id", "states")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.states).features)
    .enter().append("path")
    .attr("d", path);
     
svg.append("path")
    .datum(topojson.mesh(us, us.objects.states), 
            function (a,b) { return a !== b })
    .attr("d", path)
    .attr("id", "states");
```
In the CSS portion of the document assign the `fill` of `#states` to `#e1e1e1` and the `stroke` to `#000`. 

## Step 3: Add the data!!!

Now that our map is looking pretty slick, we can add or data! To do this we will use `d3.queue`. D3 asynchronously loads data, meaning that other svg elements in the JavaScript function can be drawn on the page in case something goes wrong with loading the data. Before we get started with queueing our data, comment out everything inside the `d3.json`. 

To create our queue we will first call `d3.queue()` and give a bunch of tasks to `defer`. The first task we want to defer is our call to `d3.json` to which we will pass the URL of our `us.json` file. The second task we want to defer is our call to `d3.csv` for loading in the `camp_map.csv` on the page of the Gist. If the defered tasks haven't thrown an error, the queue will pass the results to a callback function (`ready`). This is always the last method you will use on `d3.queue`. 

```JavaScript
d3.queue()
    .defer(d3.json, "https://gist.githubusercontent.com/cypranowska/b17359016fd22b81914fd2031cb301f0/raw/9fcd2c3e60c74e8ce8d5c2385d2961f06d815bb9/us.json")
    .defer(d3.csv, "https://gist.githubusercontent.com/cypranowska/b17359016fd22b81914fd2031cb301f0/raw/9fcd2c3e60c74e8ce8d5c2385d2961f06d815bb9/camp_map.csv")
    .await(ready);
   

function ready(error, us, camp) {
    if (error) throw error;
    
    console.log(camp);
};
```

The first argument of the callback function should evaluate to `null` if everything worked or an error if something went wrong. The remaining arguments are the output of the defered tasks in the order they are chained onto `d3.queue`.

To get our map back, copy-paste the code that creates the `topojson.feature` and `topojson.mesh` svg elements inside the callback function. 

Now, we're ready to finally map our campground data! The `camp_map.csv` file contains the latitude and longitude values for each federally-run campground on recreation.gov, along with the campground name, ID, number of campsites, percent tent-only sites, and agency name. We're going to represent the location of each campground as a circle on our map. 

Start by creating a virtual selection of circles within our svg object (inside the callback function), and bind the campground data to the selection. 

```JavaScript
svg.selectAll("circle")
    .data(camp)
    .enter().append("circle");
```

Next, we will assign the `"cx"` and `"cy"` attributes of each circle to the `lon` and `lat` values in the .csv file. However, we can't simply write `.attr("cx", function(d) { return d.lon })` and call it a day. We need to convert the longitude/latitude values to the projection used in our svg object. Instead, we pass both `d.lon` and `d.lat` to our `projection`. This will return the x and y values for each pair of `d.lon` and `d.lat` values. 

```JavaScript
svg.selectAll("circle")
    .data(camp)
    .enter().append("circle")
    .attr("cx", function(d) { return projection([d.lon, d.lat])[0]; })
    .attr("cy", function(d) { return projection([d.lon, d.lat])[1]; })
    .attr("r", 3);
```

Phew! We now have the basic information from our .csv file on our map! Try experimenting with the size of each circle, styling of each elements, legends, etc.

Congratulations on making a map in D3!

### Pearls of wisdom
If you get stuck...
* use the web inspector
* try logging to the console
* use Google