library(ggplot2)

shinyServer(function(input, output, session){
datasetInput <- reactive({ switch(input$dataset, "iris" = iris, "diamonds" = diamonds) }) 
output$summary <- renderPrint({ 
	dataset <- datasetInput() 
	summary(dataset) }) 

  output$x_value <- renderUI({
    selectInput("x_value", "X", names(datasetInput()))
  })

    output$y_value <- renderUI({
    selectInput("y_value", "Y", names(datasetInput()))
  })

    output$color <- renderUI({
    selectInput("color", "Color of variable", names(datasetInput()))
  })


output$table <- renderTable({ head(datasetInput(), n = input$obs) })
output$plot <- renderPlot({
	if (nrow(datasetInput())==0) {
		return() 
		} else {
	   ggplot(datasetInput(), aes_string(input$x_value, input$y_value)) + geom_point(aes_string(color = input$color))
	   	}
	})
	})