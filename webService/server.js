const express = require('express')
const mongoose = require('mongoose')

const articleRouter = require('./routes/articles')
const app = express()

app.set('view engine', 'ejs')
app.use('/articles', articleRouter)

app.get('/',(req,res) => {
    res.render('articles/index')
})

app.listen(5000)
