const express = require('express')
const mongoose = require('mongoose')

const articleRouter = require('routes/articles')
const app = express()

app.set('view engine', 'ejs')
app.use('/articles', articleRouter)

app.get('/',(req,res) => {
    const articles = [{
	title:'article',
	createdAt: Date.now(),
	description: 'Test description'
    }]
    res.render('index', { articles: articles })
})

app.listen(5000)
