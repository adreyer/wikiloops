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
      if(!cobj || !cobj.links){// deadend
        return path;
      }
      if(cobj.path){// already computed
        return path.concat(cobj.path);
      }
      if(contains(path, cobj.links[0])){// loop
        path[path.length] = cobj.links[0];
        return path;
      }
      path[path.length] = cobj.links[0];
      var prev_path = path.length - 2;
      var npath = flhelp(cobj.links[0], path);
      cobj.path = npath.slice(prev_path);
      db[coll].save(cobj)
      return npath;
    }

    return flhelp(name, [name]);

var replace_redirects = function replace_redirects(coll){
    var fix_redirect = function (x){
        var from = x.name;
        var to = x.links
        var fix_one = function (x){
            for(i=0;i<x.links.length;i++){
                if(x.links[i] === from){
                    x.links[i] = to;
                };
            };
        };
        db[coll].find({link: from}).forEach(fix_one);
    };

    db[coll].find({redirect=true}.forEach(fix_redirect);
};
