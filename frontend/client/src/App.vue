<template>
  <div id="app">
    <div id="test">
      <router-view></router-view>
    </div>

    <router-link to="/impressum" id="linkImpressum"><a>Impressum</a></router-link>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
}
</script>

<style>

/* #test {
  height: 100vh;
} */
#linkImpressum {
  bottom: 10px;
  position: absolute;
  margin-right: auto;
  margin-left: auto;
  text-align: center;
}
#app {
  height: 100vh;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
