<template>
  <div class="personalPosts">
    <h1>{{ msg }}</h1>
    <h2>h2 personal posts page</h2>
    <prefNavigation></prefNavigation>

  </div>
</template>

<script>
import prefNavigation from './prefNavigation'

export default {
  name: 'personalPosts',
  data () {
    return {
      msg: 'this is the message from the personal posts page'
    }
  },
  components: {
    prefNavigation
  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #personalPosts {
    float: left;
  }
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
