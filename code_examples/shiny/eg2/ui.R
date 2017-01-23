
shinyUI(fluidPage(
titlePanel("foo"),
sidebarLayout(
	sidebarPanel(
		selectInput("x", "X variable", names(iris)),
		selectInput("y", "Y variable", names(iris)),
		numericInput("size", "Size of points", 3, 1, 10, step = 2),
		checkboxInput("color", "Color By Species", TRUE)
		),
	mainPanel(
		plotOutput("plot")
		)

	)


	))