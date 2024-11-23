# Databricks notebook source
aux = dbutils.widgets.text("Texto", "Marai" )
full_name = f"{name} {aux}"



