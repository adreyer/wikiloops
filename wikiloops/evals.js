var find_loop = function (name, coll){

  var contains = function(arr, val){
    for(i=0;i<arr.length;i++){
        if(val == arr[i]){
          return true;
        }
    }
    return false;
  }

    var flhelp = function(cname, path){
      var cobj = db[coll].findOne({name: cname});
      if(!cobj || !cobj.links){
        return path
      }
      if(contains(path, cobj.links[0])){
        path[path.length] = cobj.links[0];
        return path;
      }
      path[path.length] = cobj.links[0];
      return flhelp(cobj.links[0], path);
    }

    var path = flhelp(name, [name]);
    return path
}
