// Module Setting
var express = require('express');
var router = express.Router();
var bodyParser = require('body-parser');
var mysql = require('mysql');

// mysql Connection
var conn = mysql.createConnection({
	host : "127.0.0.1",
	user : "root",
	password : "1111",
	database : "sdadb"
})

// mysql Connect
conn.connect();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get("/:id", function(req,res){
	var sql = `SELECT * FROM recipe WHERE bread_id='${req.params.id}'`;
	conn.query(sql,function(err,rows,fields){
		if(err){
			console.log(err);
		}else{
			res.send(rows);
		}
	})
});

module.exports = router;

