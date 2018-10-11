<template>
  <div class="cms">
    <h1>now im on the cms from </h1>
    <p>
      {{ userData }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'cms',
  data() {
    return {
      id: this.$route.params.id,
      userData: {}
    }
  },
  created() {
    this.$http.get('http://127.0.0.1:5000/api/user/' + this.id).then(function(data){
      console.log(data.body);
      this.userData = data;
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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


<!-- http://127.0.0.1:5000/api/user/ http://jsonplaceholder.typicode.com/posts/ -->
