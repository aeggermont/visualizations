"use strict";
 

/*  --------  GLOBAL VARIABLES -------- */

// country,gdp,medalcount,gold,silver,bronce,numathletes,population
// var margin = {top: 100, right: 20, bottom: 40, left: 0},
var margin = {top: 80, right: 120, bottom: 50, left: 120},
    TABLE_MAX_SIZE = 72,
    width = 970 - margin.left - margin.right,
    height = 450 - margin.top - margin.bottom,
    legendHeight = 15,
    normalAxis = d3.svg.axis().orient("left"),
    normalRightAxis = d3.svg.axis().orient("right"),
    percentFormat = d3.format(".0%"),
    percentAxis = d3.svg.axis().orient("left").tickFormat(percentFormat),
    rightAxis = d3.svg.axis().orient("right"),
    dimensions = ["GDP", "MedalCount", "Gold", "Silver","Bronze","AthletesCount", "Population"],
    searchString = "", hovering = [];

var axis = {
  GDP: {
    title: "GDP",
    axis: normalAxis
  },
  MedalCount: {
    title: "Medal Count",
    axis: normalAxis
  },
  Gold: {
    title: "Gold Medals",
    axis: normalAxis
  },
  Silver: {
    title: "Silver Medals",
    axis: normalAxis
  },
  Bronze: {
    title: "Bronze Medals",
    axis: normalAxis
  },
  AthletesCount: {
    title: "Num Athletes",
    axis: normalAxis
  },
  Population: {
    title: "Population",
    axis: normalRightAxis
  }
};


/*  --------  D3 VISUALIZATION COMPONENTS-------- */
var lineColor = "linecolor"


/*********  DASHBOARD LABELS  *********/

var tip = d3.select(".tip");

/**
 * Info labels element displays all labels 
 * as defined in the legend elements
 */
var legend = d3.select("#info-labels").append("svg")
    .attr("height", legendHeight)
    .attr("width", width)
  .append("g")
    .attr("transform", "translate(" + margin.left + ",0)");


/**
 * Color palette label in a rect SVG element
 *  based on 0 to 30 range, which matches array element
 * count in srm2rgb file
 */
/*
legend.selectAll("rect")
    .data(d3.range(0, 30))
    .enter()
  .append("rect")
    .attr("y", 0)
    .attr("x", function (d) { 
      return (30 - d) * 2; 
    })
    .attr("height", legendHeight)
    .attr("width", 2)
    .attr("fill", window.srm2rgb); */



    
var legendLeft = legend.append("text")
    .style("text-anchor", "start")
    .style("font-size", 12)
    .attr("x", -100)
    .attr("y", legendHeight / 2 + 6);

//legendLeft.append("tspan").text("Line Color").attr("class", "em");
//legendLeft.append("tspan").text(" indicates country color");

//legendLeft.append("tspan").text("Select a Seasson");

var legendMiddle = legend.append("text")
    .style("text-anchor", "middle")
    .style("font-size", 12)
    .attr("x", (width - margin.right) / 2)
    .attr("y", legendHeight / 2 + 6);

//legendMiddle.append("tspan").text("Click and drag on the axes").attr("class", "em");
//legendMiddle.append("tspan").text(" to filter");

var legendRight = legend.append("text")
    .style("text-anchor", "end")
    .style("font-size", 12)
    .attr("x", width - margin.left)
    .attr("y", legendHeight / 2 + 6);

//legendRight.append("tspan").text("Type in the search box").attr("class", "em");
//legendRight.append("tspan").text(" to find a country");

 /*********  END OF LEGEN LABELS  *********/

 function loadVisualizationTemp(selectedYear, selectedSeason){
          
  var dataFileIn = "data/olympic-data-" + selectedYear + "-" + selectedSeason + ".csv";
  
  ////console.log(">>>> FILE IN <<<<");
  ////console.log(dataFileIn);

  d3.csv(dataFileIn, function (countries) {
    var x = d3.scale.ordinal().rangePoints([0, width], 0.1),
    y = y || {},
    line = d3.svg.line().interpolate("cardinal");

    x.domain(dimensions);
    dimensions.forEach(function (d) {
      y[d] = (y[d] || d3.scale.linear())
        .domain(d3.extent(countries, function (p) { return +p[d]; }))
        .range([height, 0]);
    });
    
  });

}
  

function loadVisualization(selectedYear, selectedSeason){
          
  //var dataFileIn = "data/olympic-data-" + selectedYear + "-Winter.csv";
  var dataFileIn = "data/olympic-data-" + selectedYear + "-" + selectedSeason + ".csv";
  
  ////console.log(">>>> FILE IN <<<<");
  ////console.log(dataFileIn);

  try {
    var element = document.getElementById("d3chart");
    element.parentNode.removeChild(element);
  }catch(error) {}

  /**
   * Creates the main SVG container
   */
  var svgContainer = d3.select("#main_chart").append("svg")
      .attr("width", width + margin.right + margin.left)
      .attr("height", height + margin.bottom + margin.top)
      .attr("id", "d3chart")
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
  //d3.exit().remove();

  // read input data, render chart, and setup listener to re-render on resize
  d3.csv(dataFileIn, function (countries) {
    // Setup dimensions and scales
    var x = d3.scale.ordinal().rangePoints([0, width], 0.1),
        y = y || {},
        line = d3.svg.line().interpolate("cardinal");

    // Extract the list of dimensions and create a scale for each.
    console.log(">>> dimensions <<<");
    console.log(dimensions);

    x.domain(dimensions);

    dimensions.forEach(function (d) {
      y[d] = (y[d] || d3.scale.linear())
        .domain(d3.extent(countries, function (p) { 
      
          if ( d == "Population") {
            //console.log(p);
            //console.log(d);
            console.log(+p[d]);
          }
          return +p[d]; 
        }))
        .range([height, 0]);
    });

    
    // Create and render all unhighlithed country lines
    ////console.log(lineColor)
    
    // Create and render all of the faded lines
    svgContainer.append("g")
      .attr("class", "background")
      .selectAll("path")
        .data(countries)
      .enter().append("path")
        .attr("d", path);

    /*
    svgContainer.append("g")
      .attr("class", lineColor) 
      .selectAll("path")
      .data(countries)      
      .enter().append("path")
      .each(function (d) {
        ////console.log('*** rendering line:');
        //console.log(d);
        lineColor = "goldlinecolor";
        d.line = d3.select(this);
        //d.line.attr("class", this.lineColor).enter()
        //console.log(">>> unhighlithed line: <<<");
        //console.log( d);
      })
      .attr("d", path)
      .attr("class", lineColor); */
    

    // Create and render all of the 
    // foreground lines that can be 
    // selected
    var lines = svgContainer.append("g")
      .attr("class", "foreground")
      .selectAll("path")
      .data(countries)
      .enter().append("path")
      .attr("stroke", srmColor)
      .each(function (d) { 
          d.line = d3.select(this);
          //console.log(">>> foreground line :");
          //console.log(d); 
      })
      .attr("d", path)
      .on("mouseover", mouseover)
      .on("mouseout", mouseout)
      .on("mouseleave", mouseout);
    

    // Add a group element for each dimension.
    var g = svgContainer.selectAll(".dimension")
        .data(dimensions)
      .enter().append("g")
        .attr("class", function (d) { return "dimension " + d; })
        .attr("transform", function (d) { return "translate(" + x(d) + ")"; });

    // Add an axis and title.
    g.append("g")
        .attr("class", "axis")
        .each(function (d) { d3.select(this).call(axis[d].axis.scale(y[d])); })
      .append("text")
        .attr("text-anchor", "middle")
        .attr("y", -9)
        .text(function (d) { return axis[d].title; });

    // Add and store a brush for each axis.
    g.append("g")
        .attr("class", "brush")
        .each(function (d) {
          y[d].brush = (y[d].brush || d3.svg.brush());
          d3.select(this).call(y[d].brush.y(y[d]).on("brush", brush));
          d3.select("." + d + " .brush").call(y[d].brush.extent(y[d].brush.extent()));
        })
      .selectAll("rect")
        .attr("x", -8)
        .attr("width", 16);

    brush();

    // apply the correct color to use for a beer based on its SRM
    function srmColor(d) {
      return window.srm2rgb(d['Continent']);
    }

    // Returns the path for a given data point.
    function path(d) {
      return line(dimensions.map(function (p) { return [x(p), y[p](d[p])]; }));
    }

    // Handles a brush event, toggling the display of foreground lines and updating list
    function brush() {
      mouseout();
      var actives = dimensions.filter(function (p) { return !y[p].brush.empty(); }),
          extents = actives.map(function (p) { return y[p].brush.extent(); }),
          re = new RegExp("\\b" + d3.requote(searchString), "i"),
          activelist = [];

      lines.classed("fade", function (d) {
        return !actives.every(function (p, i) {
          return extents[i][0] <= d[p] && d[p] <= extents[i][1];
        }) || !re.test(d.name) || !activelist.push(d);
      });
      updateBeerList(activelist);
      hovering.forEach(hoveroutcell);
    }

    // display the country list
    function updateBeerList(activelist) {
      d3.select("#count").text(activelist.length);
      d3.select("#total").text(countries.length);
      activelist
        .sort(function (a, b) { return d3.ascending(a.name, b.name); })
        .sort(function (a, b) { return d3.descending(a.Population, b.Population); });
      activelist = activelist.slice(0, TABLE_MAX_SIZE);

      // update existing rows
      var list = d3.select("#beer-list")
        .selectAll(".beer")
        .data(activelist)
        .call(createTableRow);

      // create new rows
      list.enter()
        .append('div')
        .call(createTableRow);

      // remove old rows
      list.exit().remove();
    }

    // on mouseover data, add hover class to line and row
    function hoverovercell(d) {
      d.line.classed('hover', true).moveToFront();
      if (d.row) { d.row.classed('hover', true); }
      hovering.push(d);
    }

    // on mouseout of data, remove hover class from line and row
    function hoveroutcell(d) {
      d.line.classed('hover', false);
      if (d.row) { d.row.classed('hover', false); }
      hovering = hovering.filter(function (e) { return d !== e; });
    }

    // creates table listing all countries
    function createTableRow(row) {
      row.attr('class', 'beer')
        .style('color', srmColor)
        .html("")
        .on('mouseover', hoverovercell)
        .on('mouseout', hoveroutcell)
        .each(function (d) { d.row = d3.select(this); });

      addCell(row, 'name', 'name');
      dimensions.forEach(function (d) { addCell(row, d, d, axis[d].axis.tickFormat()); });
    }

    // creates a cell in the table
    function addCell(row, clazz, attr, format) {
      format = format || function (d) { return d; };
      row.append("div")
        .attr('class', clazz)
        .text(function (d) { return format(d[attr]); });
    }


    // setup search

    var searchInput = d3.select(".search input")
        .on("keyup", function () {
          if (d3.event.keyCode === 27) {
            this.value = "";
            this.blur();
          }
          search(this.value.trim());
        });

    var searchClear = d3.select(".search .search-clear")
        .on("click", function () {
          searchInput.property("value", "").node().blur();
          search();
        });

    function search(value) {
      searchString = value || "";
      searchClear.style("display", value ? null : "none");
      brush();
    }

    /**
     * Legends in mouse over events 
     * @param {*} d 
     */
    function mouseover(d) {       
      if (d.mouseover) { return; }
      mouseout();
      d.mouseover = true;

      console.log(">>> lines <<<");

      lines.filter(function (c) { return c === d; })
        .classed("active", true)
        .each(function () {
          //console.log(this);
          this.parentNode.appendChild(this);
        });
      
      var dx = d3.mouse(svgContainer.node())[0],
          dy = d3.mouse(svgContainer.node())[1];

      
      // Render tooltip in each line
      tip.style("display", null)
          .style("top", (dy + (margin.top + 80)  - (+tip.style("height").replace("px", "")) - 5) + "px")
          .style("left", (dx + (margin.left + 250) - (+tip.style("width").replace("px", "")) - 5) + "px");

      tip.select("#athleteCount").text(d.AthletesCount);
      tip.select("#medalCount").text(d.MedalCount);
      tip.select("#goldMedalsCount").text(d.Gold);
      tip.select("#silverMedalCount").text(d.Silver);
      tip.select("#bronzeMedalCount").text(d.Bronze);
      
      tip.select("#totalPopulation").text( function () {
        return d.Population.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      });
      
  
      tip.select("#totalGDP").text( function () {
        if (d.GDP === '0') {
          return "Not available"
        } else {
          return d.GDP.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }
      });

      var name = d.name.length > 40 ? d.name.substr(0, 40) + "..." : d.name;
      tip.selectAll(".name").text(name);
      
    }


    function testGDP(gpd) {
      console.log("testing GDP");
      console.log(gdp);
    }  

    function mouseout() {
      tip.style("display", "none");
      lines.filter(".active")
        .classed("active", false)
        .each(function (d) { 
          d.mouseover = false; 
        });
    }
  });
}

// add utility to move an SVG selection to the front
d3.selection.prototype.moveToFront = function () {
  return this.each(function () {
    this.parentNode.appendChild(this);
  });
};



/*  --------  INTERACTIVE NAVIGATION -------- */
var baseYear  = parseInt(1980);
var yearIntervals = 4;
var selectedYear = 1980;        // Default Year
var selectedSeason = "Winter";  // Default season
var dataInputFile = "data/olimpics_data_" + selectedYear + ".csv";

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var seasson = document.getElementById("seasson");
var sliderLeyend = document.getElementById("eventYear");

var prevYear;

//var base_year = 1980
output.innerHTML = baseYear;
seasson.innerHTML = selectedSeason;
sliderLeyend.innerHTML = selectedYear;

slider.oninput = function() {

  prevYear = selectedYear;
  
  if ( ( parseInt(selectedYear) >= 1992) && ( selectedSeason == "Winter")) {  
    selectedYear = baseYear + ( (yearIntervals * parseInt(this.value)) - 2);   
  } else if ( (parseInt(prevYear) == 1994) && ( parseInt(prevYear) > parseInt(selectedYear)  )) {
    //console.log(" pprevious year was 1994!");
  } else {
    selectedYear = baseYear + (yearIntervals * parseInt(this.value));
  }

  output.innerHTML = selectedYear;
  sliderLeyend.innerHTML = selectedYear;
  loadVisualization(selectedYear, selectedSeason);
}


$(document).ready(function() {
  loadVisualization(1980, "Winter");

  $("#summer").bind("click", function() { 
    selectedSeason = "Summer";
    seasson.innerHTML = selectedSeason;
    loadVisualization(selectedYear, selectedSeason);
  }); 

  $("#winter").bind("click", function() { 
    selectedSeason = "Winter";
    seasson.innerHTML = selectedSeason;
    loadVisualization(selectedYear, selectedSeason);
  }); 

});