
const router = require('express-promise-router')();
const acces = require('../node_scripts/hasAcces')

app.get("/", acces.hasAcces, function(req,res){
        //res.render('index',{name:"Beta"})    
        res.render('index',{name:req.session.userObject.fullName})    
});

module.exports = router