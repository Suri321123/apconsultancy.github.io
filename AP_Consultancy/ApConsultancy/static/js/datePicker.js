
(function() {
  var app = angular.module("myApp", ['ngSanitize']);
app.controller("myCtrl", function($scope) {
    $scope.myText = "My name is: <h1>John Doe</h1>";
});

});
/**
Copyright 2018 Google Inc. All Rights Reserved. 
Use of this source code is governed by an MIT-style license that can be foundin the LICENSE file at http://material.angularjs.org/HEAD/license.
**/