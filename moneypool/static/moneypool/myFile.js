
var moneypoolModule=angular.module('monpoModule',[]);

        moneypoolModule.controller('myCtrl',['$scope','$http',function($scope,$http){
			

            $scope.mydata=[];
            $http.get('/moneypool/masterprofile/').then(function(response){
                $scope.data=response.data;
            });
            console.log($scope.data);
            $scope.show=false;
            $scope.id;
           $scope.showDiv = function (_id) {
                //If DIV is visible it will be hidden and vice versa.
                console.log(_id);
                //$scope.id=_id;
                //console.log($scope.id);
                $scope.show = $scope.show?false:true;
                 var requestUrl = '/moneypool/profile/' + _id ;
                $http.get(requestUrl).then(function(resp) {
                   $scope.mydata=resp.data;
                });
                console.log()
            }

            $scope.hideDiv = function (_id) {
                $scope.show=($scope.show==true)?false:true;
                var requestUrl = '/moneypool/masterprofile/' + _id ;
                $http.get('/moneypool/masterprofile/').then(function(response){
                $scope.mydata=response.data;
            });

            }

             $scope.existing_profiles=[];
             $scope.data=[];
              console.log($scope.existing_profiles);
                $scope.getById=function(id) {
                console.log('inside function');
                var requestUrl = '/moneypool/profile/' + id ;
                $http.get(requestUrl).then(function(resp) {
                   $scope.existing_profiles.push(resp.data);
                });
            };

            console.log($scope.existing_profiles);
            $scope.add=function(p_no,name,rsp,mail,add1,add2,pin,age){
                var postdata={
                    phone_number:p_no,
                    group_id:$scope.existing_profiles.group_id,
                    name:name,
                    relationship:rsp,
                    mail_id:mail,
                    address_1:add1,
                    address_2:add2,
                    pincode:pin,
                    custom_filter:' ',
                    customer_type:' ',
                    vendor_type:' ',
                    card_number:' ',
                    expiry:' ',
                    age:age,
                    name_on_card:' '
                };
                $http.post('/moneypool/profile/',postdata)
                      .then(function(response){
                        existing_profiles.push(postdata);
                      });
                     console.log($scope.existing_profiles);



            };



        }]);


