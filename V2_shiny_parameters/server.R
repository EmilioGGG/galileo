library(shiny)

shinyServer(function(input, output, session) {
  
  observe({
    query <- parseQueryString(session$clientData$url_search)
    bins <- query[['bins']]
    bar_col <- query[['color']]
    set_col <- query[['color']]
    if(!is.null(bins)){
      updateSliderInput(session,'bins',value=as.numeric(bins))
    }
    if(!is.null(bar_col)){
      updateSliderInput(session,'set_col',value = bar_col)
    }
  })


  
output$distPlot <- renderPlot({
  x <-  faithful[,2]
  plot(x, col=input$set_col)
  })

output$click_data <- renderPrint({
  
  rbind(c(input$clk$x, input$clk$y,updateSliderInput(session,'set_col',value = 'aquamarine')),
        c(input$dclk$x, input$dclk$y, updateSliderInput(session,'set_col',value = 'white'), update),
        c(input$mouse_hover$x,input$mouse_hover$y,updateSliderInput(session,'set_col',value = 'darkgray')),
        c(input$mouse_brush$xmin,input$mouse_brush$ymin, updateSliderInput(session,'set_col',value = 'aquamarine')),
        c(input$mouse_brush$xmax,input$mouse_brush$ymmax, updateSliderInput(session,'set_col',value = 'aquamarine'))
  )
})

output$dclick_data <- renderPrint({
  
  rbind(c(input$dclk$x, input$dclk$y, updateSliderInput(session,'set_col',value = 'white'))
  )
})


output$mouse_hover_data <- renderPrint({
  
  rbind(
        c(input$mouse_hover$x,input$mouse_hover$y,updateSliderInput(session,'set_col',value = 'darkgray'))
  )
})

output$mouse_brush_data <- renderPrint({
  
  rbind(c(input$mouse_brush$xmin,input$mouse_brush$ymin, updateSliderInput(session,'set_col',value = 'aquamarine')),
        c(input$mouse_brush$xmax,input$mouse_brush$ymmax, updateSliderInput(session,'set_col',value = 'aquamarine'))
  )
})





})
