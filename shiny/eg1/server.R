library(shiny)
library(ggplot2)


shinyServer(function(input, output) {
  output$distPlot <- renderPlot({
    if(!input$color) {
    ggplot(iris, aes_string(x=input$x, y=input$y)) + geom_point(size = input$size)
    } else {
        ggplot(iris, aes_string(x=input$x, y=input$y)) + geom_point(aes(color = Species), size = input$size)
    }
  })
})