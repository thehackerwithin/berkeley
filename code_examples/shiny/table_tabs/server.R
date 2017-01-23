library(ggplot2)

shinyServer(function(input, output){
datasetInput <- reactive({ switch(input$dataset, "iris" = iris, "diamonds" = diamonds) }) 
output$summary <- renderPrint({ 
	dataset <- datasetInput() 
	summary(dataset) }) 
output$table <- renderTable({ head(datasetInput(), n = input$obs) })
output$plot <- renderPlot({
	   ggplot(iris, aes(Sepal.Length, Sepal.Width)) + geom_point()
	})
	})