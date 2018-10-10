<template>
  <div class="personalInformation">
    <h1>{{ msg }}</h1>
    <h2>h2 personal information page</h2>
    <prefNavigation></prefNavigation>

    <div>
      <b-form-group label="Radios using <code>options</code>">
        <b-form-radio-group id="radios1" v-model="selected" :options="options" name="radioOpenions">
        </b-form-radio-group>
      </b-form-group>
      <b-form-group label="Radios using sub-components">
        <b-form-radio-group id="radios2" v-model="selected" name="radioSubComponent">
          <b-form-radio value="first">Toggle this custom radio</b-form-radio>
          <b-form-radio value="second">Or toggle this other custom radio</b-form-radio>
          <b-form-radio value="third" disabled>This one is Disabled</b-form-radio>
          <b-form-radio :value="{fourth: 4}">This is the 4th radio</b-form-radio>
        </b-form-radio-group>
      </b-form-group>

      <div class="mt-3">
        Selected: <strong>{{ selected }}</strong>
      </div>
    </div>
  </div>
</template>

<script>
import prefNavigation from './prefNavigation'

export default {
  name: 'personalInformation',
  data () {
    return {
      msg: 'this is the message from the personalInformation page',
      selected: 'first',
      options: [
        { text: 'Toggle this custom radio', value: 'first' },
        { text: 'Or toggle this other custom radio', value: 'second' },
        { text: 'This one is Disabled', value: 'third', disabled: true },
        { text: 'This is the 4th radio', value: {fourth: 4} }
      ]
    }
  },
  components: {
    prefNavigation
  }
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #personalInformation {
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
