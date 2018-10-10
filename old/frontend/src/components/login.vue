<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>please login here</p>
    <input type="email" v-model="inputEmail" placeholder="Email adresse" />
    <input type="password" v-model="inputPassword" placeholder="Passwort" />
    <router-link to="/mainPage"><button>Login</button></router-link>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      msg: 'Welcome to the sample App',
      inputEmail: undefined,
      inputPassword: undefined
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
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
