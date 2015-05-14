library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

  # Application title
  titlePanel("Hello Iris!"),
  br(),

  # Sidebar with a slider input for the number of bins
  h4("This are example controls"),
sidebarLayout(
    sidebarPanel(
  selectInput("x", "Choose x variable:",
            c("Sepal Length" = "Sepal.Length",
              "Sepal Width"  = "Sepal.Width",
              "Petal Length"  = "Petal.Length",
              "Petal Width"  = "Petal.Width"), width = 200, selected = "Petal.Length"),
  selectInput("y", "Choose y variable:",
            c("Sepal Length" = "Sepal.Length",
              "Sepal Width"  = "Sepal.Width",
              "Petal Length"  = "Petal.Length",
              "Petal Width"  = "Petal.Width"), width = 200),
  checkboxInput("color", "Color by Species",  TRUE),
  # sliderInput("size",
  #                 "Point Size:",
  #                 min = 1,
  #                 max = 10,
  #                 value = 3),

    numericInput("size", "Point Size", 4, 1, 15, step =1)
    ),

    # Show a plot of the generated distribution
    mainPanel(
      h2("This is a title for the plog"),
      plotOutput("distPlot"),
      p("Dead digital drugs saturation point military-grade savant katana receding plastic grenade pen pistol shoes. Otaku sub-orbital shoes franchise render-farm RAF-space human Chiba paranoid papier-mache sprawl hotdog narrative saturation point dissident. Motion bomb spook realism convenience store long-chain hydrocarbons gang smart-artisanal franchise office systema order-flow wonton soup towards cyber-sentient. Sign woman pen-ware Kowloon refrigerator warehouse knife towards urban smart-papier-mache. BASE jump 3D-printed Chiba cardboard wristwatch construct hacker. Faded sign modem tank-traps nodality meta-knife dissident. ")
    )
  )
))