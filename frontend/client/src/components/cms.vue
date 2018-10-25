<template>
  <div class="cms">
    <cmsTitle
      v-model="pageTitle"
      v-bind:titleColor="titleColor"></cmsTitle>
    <preferences
      v-model="titleColor"></preferences>
  </div>
</template>

<script>
import cmsTitle from './cmsTitle'
import preferences from './preferences'

export default {
  name: 'cms',
  data() {
    return {
      id: this.$route.params.id,
      pageTitle: "",
      pageTitleOld: "",
      titleColor: "",
      userData: {
        id: '',
        title: this.pageTitle,
        titleColor: this.titleColor,
      },
    }
  },
  components: {
    cmsTitle,
    preferences,
  },
  methods: {
    postSubmitToServer: function(titleColor){
      // this.$http.post(`http://127.0.0.1:5000/auth/content`, {
      //   userData:this.pageTitle
      // });
    },
  },
  // created() {
  //   this.$http.get('http://127.0.0.1:5000/auth/content').then(function(data){
  //     console.log(data);
  //     this.userData = data;
  //   });
  // },
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
