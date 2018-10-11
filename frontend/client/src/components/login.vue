<template>
  <div class="login">
    <!-- <h1>{{ msg }}</h1> -->
    <h1>login</h1>


    <input type="text" v-model="login.name" placeholder="Name" />
    <input type="password" v-model="login.password" placeholder="Passwort" />
    <!-- <router-link to="/cms"><button>Login!</button></router-link> -->
    <button v-on:click.prevent="loginEvent">Login</button>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'login',
  data() {
    return {
      login:{
        name:'',
        password:''
      },
      user:{
        secret:'',
        id:'',
        name:''
      }
    }
  },
  methods: {
    getData(secret){
      console.log(secret)
      
    },
    loginEvent: function(){
      const qs = require('qs');
      axios.post(`http://127.0.0.1:5000/api/login/`, qs.stringify({ 'name': this.login.name, 'password': this.login.password }))
      .then(response => {
        this.user.secret = response;
        this.getData(response)
      })
    },

  }
}
</script>


<style scoped>

  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
