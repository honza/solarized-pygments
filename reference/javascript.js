// This is a test


(function() {

  String.prototype.reverse = function() {
    return this.split('').reverse().join('');
  };

  var a = {
    name: 'Honza',
    email: 'me@honza.ca',
    count: 23
  };

  var pattern = /([a-z]+)/;

  var name = "Honza";
  var doSomething = function(array) {
    if (array.length >= 0) {
      return array;
    }
    return false;
  };

}).call(this);
