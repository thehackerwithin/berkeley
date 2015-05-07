library(ggplot2)

shinyServer(function(input, output){
datasetInput <- reactive({ switch(input$dataset, "iris" = iris, "diamonds" = diamonds) }) 
output$summary <- renderPrint({ 
	dataset <- datasetInput() 
	summary(dataset) }) 
output$view <- renderTable({ head(datasetInput(), n = 10) })

	})