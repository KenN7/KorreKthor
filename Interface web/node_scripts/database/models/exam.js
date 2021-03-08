'use strict';
const {
  Model,
  Sequelize
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Exam extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate({ User, Copy }) {
      // define association here
      this.belongsTo(User, {foreignKey:"userId", as:"user"})
      this.hasMany(Copy, {foreignKey:"examId", as:"copies"})
    }
  };
  Exam.init({
    id: {
      type: DataTypes.UUID,
      defaultValue: Sequelize.UUIDV4,
      primaryKey: true,
    },
    name: {
        type: DataTypes.STRING,
        allowNull: false
    },
    numberOfVersion:{
        type: DataTypes.INTEGER,
        allowNull: false
    },
    versionsFiles:{
        type: DataTypes.ARRAY(DataTypes.STRING),
    },
    correctionFiles:{
        type: DataTypes.ARRAY(DataTypes.STRING),
    },
    examFile:{
        type: DataTypes.STRING,
    },
  }, {
    sequelize,
    tableName: "exams",
    modelName: 'Exam',
  });
  return Exam;
};