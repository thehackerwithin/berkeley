
shinyUI(fluidPage(
	titlePanel("test"),
	sidebarLayout(
		sidebarPanel( 
	selectInput("dataset", "Choose a dataset:",  c("iris", "diamonds")),
	submitButton("Update View")
				),
		
		mainPanel(
		tableOutput("view")
		)

	)))