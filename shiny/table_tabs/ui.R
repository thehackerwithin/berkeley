
shinyUI(fluidPage(
	headerPanel("Example with Tabs"),
	sidebarLayout(
		sidebarPanel( 
	selectInput("dataset", "Choose a dataset:",  c("iris", "diamonds")),
	numericInput("obs", "Observations:", 10),
	submitButton("Update View")
				),
		
		mainPanel(tabsetPanel( 
	tabPanel("Plot", plotOutput("plot")),
	tabPanel("Summary",verbatimTextOutput("summary")), 
	tabPanel("Table", tableOutput("table")) )) 


	)))