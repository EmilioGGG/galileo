

library(shiny)

shinyUI(fluidPage(


    titlePanel("Parametros Shiny"),
    sidebarLayout(
      sidebarPanel(
        selectInput("set_col",
                    "escoger color:",
                    choices= c('aquamarine', 'blue','blueviolet','darkgray','chocolate', 'white', 'red'),
                    selected = 'darkgray'
                    )
      ),
      mainPanel(
        plotOutput("distPlot",
                   click = "clk",
                   dblclick = 'dclk',
                   hover = 'mouse_hover',
                   brush = 'mouse_brush'),
        verbatimTextOutput('click_data'),
        verbatimTextOutput('dclick_data'),
        verbatimTextOutput('mouse_hover_data'),
        verbatimTextOutput('mouse_brush_data'),
        DT::dataTableOutput('mtcars_tbl')
      )
    )

))
