<template>
  <div id="app">
    <controlPanel
      v-model="pageTitle">
    </controlPanel>
    <preview v-bind:title="pageTitle"></preview>
    {{ pageTitleBackgroundColor }}
  </div>
</template>

<script>
import controlPanel from './components/controlPanel'
import preview from './components/preview'

export default {
  name: 'app',
  data () {
    return {
      pageTitle: "default",
      pageTitleBackgroundColor: "grey",

    }
  },
  components: {
    controlPanel,
    preview,
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
