<template>
  <div id="login">
    {{ msg }}
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      msg: "this is another instance, the login"
    }
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
