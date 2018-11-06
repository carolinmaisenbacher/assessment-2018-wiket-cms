<template>
  <div id="login">
    <!-- <h1>{{ msg }}</h1> -->
    <h1>login</h1>


    <input type="text" v-model="user.email" placeholder="E-Mail" />
    <input type="password" v-model="user.password" placeholder="Passwort" />
    <!-- <router-link to="/cms"><button>Login!</button></router-link> -->
    <button v-on:click.prevent="loginEvent">Log In</button>
    <button v-on:click.prevent="signupEvent">Sign Up</button>

  </div>
</template>

<script>


export default {
  name: 'login',
  data() {
    return {
      user:{
        email:'',
        password:'',
        id:'user id'
      },
      //failureResponse,
    }
  },
  methods: {
    getData(secret){
      console.log(secret)

    },
    loginEvent: function(){
      this.$http.post(`http://127.0.0.1:5000/auth/login`, {
        email:this.user.email,
        password:this.user.password
      }).then(function(response){
        var userId = response.data.userId;
        this.user.id = userId;
        this.$router.push({ path: '/home' })
        //this.$router.push({ name: 'cms', params: {userId }})
      }, function(response){
        console.log("failure:", response.data.error);
      });
    },
    signupEvent: function(){
      this.$http.post(`http://127.0.0.1:5000/auth/signup`, {
        email:this.user.email,
        password:this.user.password
      }).then(function(response){
        this.user.id = response.data.userId;
        console.log("user created");
      }, function(response){
        console.log("failure:", response.data.error);
      });
    },
  }
}
</script>


<style scoped>

  #login h3 {
    margin: 40px 0 0;
  }
  #login ul {
    list-style-type: none;
    padding: 0;
  }
  #login li {
    display: inline-block;
    margin: 0 10px;
  }
  #login a {
    color: #42b983;
  }
</style>
