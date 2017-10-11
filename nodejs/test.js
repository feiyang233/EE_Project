const http = require('http');
const fs=require('fs');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {

  var file_name='.'+req.url;
  console.log(req.url)
  fs.readFile(file_name,function(err,data){
  	if (err) {
  		res.write('404');
  	}else{
  		res.write(data);
  	}
  	 res.end(); 
  });
});
  //res.statusCode = 200;
  //res.setHeader('Content-Type', 'text/plain');
  server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
