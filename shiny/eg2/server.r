library(ggplot2)
data(iris)

shinyServer(function(input, output) {

output$plot <- renderPlot({
	if(!input$color) {
	ggplot(iris, aes_string(input$x, input$y)) + geom_point(size =3)
	} else {
		ggplot(iris, aes_string(input$x, input$y)) + 
		geom_point(aes(color = Species), size = input$size)
	}
	})


})